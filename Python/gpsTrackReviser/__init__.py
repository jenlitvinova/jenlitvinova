# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gpx_trackreviser
                                 A QGIS plugin
 gpx_trackreviser
                             -------------------
        begin                : 2017-05-14
        copyright            : (C) 2017 by Yevgeniya Litvinova
        email                : jenlitvinova@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load gpx_trackreviser class from file gpx_trackreviser.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gpx_trackreviser import gpx_trackreviser
    return gpx_trackreviser(iface)
