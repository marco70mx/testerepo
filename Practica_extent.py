import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for df in mapping.ListDataFrames(mxd):
    if (df.name == 'Crime'):
        layers = mapping.ListLayers(mxd,'Crime Density by School District',df)
        for layer in layers:
            query = '"NAME" = \'Lackland ISD\''
            layer.definitionQuery = query
            df.extent = layer.getExtent()
