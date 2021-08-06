# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gpx_trackreviser
                                 A QGIS plugin
 gpx_trackreviser
                              -------------------
        begin                : 2017-05-14
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Yevgeniya Litvinova
        email                : jenlitvinova@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import *
from qgis.core import *
import qgis.utils
import ogr
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from gpx_trackreviser_dialog import gpx_trackreviserDialog
import os.path

w = QWidget ()

class gpx_trackreviser:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'gpx_trackreviser_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&gpx_trackreviser')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'gpx_trackreviser')
        self.toolbar.setObjectName(u'gpx_trackreviser')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('gpx_trackreviser', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dlg = gpx_trackreviserDialog()

        # -- clearing input and output file name
        self.dlg.lineEdit.clear()
        self.dlg.lineEdit_2.clear()

        self.dlg.toolButton.clicked.connect(self.select_shp_path)
        self.dlg.toolButton_2.clicked.connect(self.select_gpx_path)

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/gpx_trackreviser/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u''),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&gpx_trackreviser'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def select_shp_path (self):
        global shp_path
        shp_path = QFileDialog.getOpenFileName(w, 'Select the SHP File', QgsProject.instance().homePath(), '*.shp')
        self.dlg.lineEdit.setText(shp_path)

    def select_gpx_path (self):
        global gpx_path
        gpx_path = QFileDialog.getOpenFileName(w, 'Select the GPX File', QgsProject.instance().homePath(), '*.gpx')
        self.dlg.lineEdit_2.setText(gpx_path)

    def add_layer_to_map (self):
        self.iface.addVectorLayer(shp_path, 'shapelayer', 'ogr')

    def rectifyTime (self, shp_path, gpx_path, loadLayer):
        shp_driver = ogr.GetDriverByName('ESRI Shapefile')
        shp_source = shp_driver.Open(shp_path, 1)
        shp_layer = shp_source.GetLayer(0)


        gpx_driver = ogr.GetDriverByName('GPX')
        gpx_source = gpx_driver.Open(gpx_path, 0)
        gpx_layer = gpx_source.GetLayerByName('track_points')

        time = []

        for feat in gpx_layer:
            time.append(feat.GetFieldAsString('time'))

        timestamp_fld = ogr.FieldDefn('timestamp', ogr.OFTString)
        timestamp_fld.SetWidth(25)
        shp_layer.CreateField(timestamp_fld)

        i = 0
        for feat in shp_layer:
            feat.SetField('timestamp', time[i])
            shp_layer.SetFeature(feat)
            i+=1

        if loadLayer:
            outputLayer = self.iface.addVectorLayer(shp_path, 'shapelayer', 'ogr')
            if not outputLayer:
                print "Layer failed to load!"

    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            #pass
            self.rectifyTime(shp_path, gpx_path, self.dlg.checkBox.isChecked())
