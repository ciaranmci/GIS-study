# Run load_layer.py script.
exec(open('C:\\Users\\medcmci\\OneDrive - University of Leeds\\Learning\\Spatiotemporal stats in R\\GIS-Study\\Lynda.com\\AGIS and Python for AEC\\load_layers.py'.encode('utf-8')).read())

# Define storage location for the buffer shape.
buffer_location = "C:\\temp\\mybuffer.shp"
    
processing.run("native:buffer",\
{'INPUT':'C:\\Users\\medcmci\\OneDrive - University of Leeds\\Learning\\Spatiotemporal stats in R\\GIS-Study\\GIS-data\\AEC with python and QGIS\\2 Managing Layers and Projects with Python\\DATA\\ROAD_CENTERLINES.shp',\
'DISTANCE':3,\
'SEGMENTS':5,\
'END_CAP_STYLE':0,\
'JOIN_STYLE':0,\
'MITER_LIMIT':2,\
'DISSOLVE':False,\
'OUTPUT':buffer_location})

iface.addVectorLayer(buffer_location,\
"(3M)",\
providerKey = "ogr")