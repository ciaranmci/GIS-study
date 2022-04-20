# Set CRS.
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(26910))
# Load vector layer.
layer = iface.addVectorLayer("C:\\Users\\medcmci\\OneDrive - University of Leeds\\Learning\\Spatiotemporal stats in R\\GIS-Study\\GIS-data\\AEC with python and QGIS\\2 Managing Layers and Projects with Python\\DATA\\ROAD_CENTERLINES.shp",\
baseName = "Roads",\
providerKey = "ogr")
# Recolour the roads as black. NB: must called the triggerRepaint() function to
# action the recolouring.
layer.renderer().symbol().setColor(QColor("black"))
layer.triggerRepaint()