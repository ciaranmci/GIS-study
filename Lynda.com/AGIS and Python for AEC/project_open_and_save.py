# Define a project object as the current project.
project = QgsProject.instance()
# Load the streetlights.qgs project into the project object.
project.read("C:\\Users\\medcmci\\OneDrive - University of Leeds\\Learning\\Spatiotemporal stats in R\\GIS-Study\\GIS-data\\AEC with python and QGIS\\2 Managing Layers and Projects with Python\\streetlight_map.qgz")
# Add road centre lines from load_layer.py script.
exec(open('C:\\Users\\medcmci\\OneDrive - University of Leeds\\Learning\\Spatiotemporal stats in R\\GIS-Study\\Lynda.com\\AGIS and Python for AEC\\load_layers.py'.encode('utf-8')).read())
# Save project.
project.write("C:\\Users\\medcmci\\OneDrive - University of Leeds\\Learning\\Spatiotemporal stats in R\\GIS-Study\\GIS-data\\AEC with python and QGIS\\2 Managing Layers and Projects with Python\\streetlight_map_new.qgz")
QgsProject.instance().clear()