# Set CRS.
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(26910))
# Add vector layer.
layer = iface.addVectorLayer(\
"C:\\Users\\medcmci\\OneDrive - University of Leeds\\Learning\\Spatiotemporal stats in R\\GIS-Study\\GIS-data\\AEC with python and QGIS\\2 Managing Layers and Projects with Python\\DATA\\EASEMENTS.shp",\
baseName = "Rights of Way",
providerKey = "ogr")
# Add raster later.
layer = QgsRasterLayer(\
"C:\\Users\\medcmci\\OneDrive - University of Leeds\\Learning\\Spatiotemporal stats in R\\GIS-Study\\GIS-data\\AEC with python and QGIS\\2 Managing Layers and Projects with Python\\DATA\\NANAIMO.ecw",\
baseName = "Aerials")
QgsProject.instance().addMapLayer(\
mapLayer = layer,\
addToLegend = False)
#Select the group object at the base of the layer tree.
layerTree = iface.layerTreeCanvasBridge().rootGroup()
# Insert the WMS layer as the base of the layer tree.
layerTree.insertChildNode(-1,QgsLayerTreeLayer(layer))
# Add XYZ.
params = "type=xyz&url=https://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0"
layer = QgsRasterLayer(params,\
baseName = "OSM",\
providerKey = "wms")
QgsProject.instance().addMapLayer(\
mapLayer = layer,\
addToLegend = False)
#Select the group object at the base of the layer tree.
layerTree = iface.layerTreeCanvasBridge().rootGroup()
# Insert the WMS layer as the base of the layer tree.
layerTree.insertChildNode(-1,QgsLayerTreeLayer(layer))