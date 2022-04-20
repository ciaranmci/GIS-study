layer = QgsProject.instance().mapLayersByName('CITY_LIMIT')[0]
features = layer.getFeatures(QgsFeatureRequest())

for f in features:
    geom = f.geometry()
    name = f.attribute('PCNAME')
    print(name)
    print('Area: (m^2)', geom.area())
    print('Perimeter: (m)', geom.length())
    print(geom.asWkt())
    print(geom.centroid().asWkt())