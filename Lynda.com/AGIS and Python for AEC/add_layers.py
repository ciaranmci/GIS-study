wkt_point = "Point(431352 5446856)"
wkt_line = "LineString(431352 5446890, 432064 5446880)"
myGeom_point = QgsGeometry.fromWkt(wkt_point)
myGeom_line = QgsGeometry.fromWkt(wkt_line)


#################################
## Define layer-maker function ##
#################################
def layerMaker(geom_obj, layer_name):
    # What type of geometry object is geom_object?
if geom_obj.wkbType() == 0:
        geom_type = 'Unknown'
        elif geom_obj.wkbType() == 1:
            geom_type = "Point"
        elif geom_obj.wkbType() == 2:
            geom_type = "LineString"
        elif geom_obj.wkbType() == 3:
            geom_type = "Polygon"
        elif geom_obj.wkbType() == 4:
            geom_type = 'WKBMultiPoint'
        elif geom_obj.wkbType() == 5:
            geom_type = 'WKBMultiLineString'
        elif geom_obj.wkbType() == 6:
            geom_type = 'WKBMultiPolygon'
        elif geom_obj.wkbType() == 7:
            geom_type = 'WKBNoGeometry'
        elif geom_obj.wkbType() == 8:
            geom_type = 'WKBPoint25D'
        elif geom_obj.wkbType() == 9:
            geom_type = 'WKBLineString25D'
        elif geom_obj.wkbType() == 10:
            geom_type = 'WKBPolygon25D'
        elif geom_obj.wkbType() == 11:
            geom_type = 'WKBMultiPoint25D'
        elif geom_obj.wkbType() == 12:
            geom_type = 'WKBMultiLineString25D'
        elif geom_obj.wkbType() == 13:
            geom_type = 'WKBMultiPolygon25D'
    
    layerPath = geom_type + "?crs=EPSG:26910"
    # Instantiate a vector layer.
    myLayer = QgsVectorLayer(\
    path = layerPath,\
    baseName = layer_name,\
    providerLib = "memory")
    # Instantiate a dataProvider object that will accept my geometry.
    dp_Layer = myPointLayer.dataProvider()
    # Instantiate a QGIS features object.
    myFeatures = QgsFeature()
    # Store my geometry in the instantiated QGIS features object.
    myFeatures.setGeometry(geom_obj)
    # Add my new features to my vector layer.
    dp_Layer.addFeatures([myFeatures])
    dp_Layer.updateExtents()
    # Add my point layer to the current project.
    QgsProject.instance().addMapLayer(myLayer)

#####################
## Add point layer ##
#####################
layerMaker(geom_obj = myGeom_point, layer_name = 'Point layer')
####################
## Add line layer ##
####################
layerMaker(geom_obj = myGeom_line, layer_name = 'Line layer')
# Instantiate a vector layer.
myPointLayer = QgsVectorLayer(\
path = "Point?crs=EPSG:26910",\
baseName = 'Point Layer',\
providerLib = "memory")
# Instantiate a dataProvider object that will accept my geometry.
dp_pointLayer = myPointLayer.dataProvider()
# Instantiate a QGIS features object.
myFeatures = QgsFeature()
# Store my geometry in the instantiated QGIS features object.
myFeatures.setGeometry(myGeom_point)
# Add my new features to my vector layer.
dp_pointLayer.addFeatures([myFeatures])
dp_pointLayer.updateExtents()
# Add my point layer to the current project.
QgsProject.instance().addMapLayer(myPointLayer)