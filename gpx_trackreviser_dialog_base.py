# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpx_trackreviser_dialog_base.ui'
#
# Created: Sun May 14 19:11:37 2017
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_gpx_trackreviserDialogBase(object):
    def setupUi(self, gpx_trackreviserDialogBase):
        gpx_trackreviserDialogBase.setObjectName(_fromUtf8("gpx_trackreviserDialogBase"))
        gpx_trackreviserDialogBase.resize(394, 215)
        self.button_box = QtGui.QDialogButtonBox(gpx_trackreviserDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 150, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.label = QtGui.QLabel(gpx_trackreviserDialogBase)
        self.label.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(gpx_trackreviserDialogBase)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(gpx_trackreviserDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 191, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(gpx_trackreviserDialogBase)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 80, 191, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.checkBox = QtGui.QCheckBox(gpx_trackreviserDialogBase)
        self.checkBox.setGeometry(QtCore.QRect(40, 120, 171, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.toolButton = QtGui.QToolButton(gpx_trackreviserDialogBase)
        self.toolButton.setGeometry(QtCore.QRect(340, 40, 31, 22))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(gpx_trackreviserDialogBase)
        self.toolButton_2.setGeometry(QtCore.QRect(340, 80, 31, 22))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))

        self.retranslateUi(gpx_trackreviserDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), gpx_trackreviserDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), gpx_trackreviserDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(gpx_trackreviserDialogBase)

    def retranslateUi(self, gpx_trackreviserDialogBase):
        gpx_trackreviserDialogBase.setWindowTitle(_translate("gpx_trackreviserDialogBase", "gpx_trackreviser", None))
        self.label.setText(_translate("gpx_trackreviserDialogBase", "Select SHP file", None))
        self.label_2.setText(_translate("gpx_trackreviserDialogBase", "Select GPX file", None))
        self.checkBox.setText(_translate("gpx_trackreviserDialogBase", "Load output layer", None))
        self.toolButton.setText(_translate("gpx_trackreviserDialogBase", "...", None))
        self.toolButton_2.setText(_translate("gpx_trackreviserDialogBase", "...", None))

