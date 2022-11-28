import os

FOLDER_NAME = "PROJECT_JSON"
MATERIALS_FOLDER = FOLDER_NAME +"/materials"
MODELS_FOLDER = FOLDER_NAME + "/models"

START = 213
END = 292
ID = 892

try: 
    os.mkdir(FOLDER_NAME)
    os.mkdir(MATERIALS_FOLDER)
    os.mkdir(MODELS_FOLDER)
except OSError as error: 
    print(error)  

### SCENE
f = open(FOLDER_NAME +"/" + "scene.json", "w+")

for i in range(START, END + 1):    
    ID = ID + 4
    f.write('{ \n')
    f.write('    "alignment" : "center", \n')
    f.write('    "alpha" : 1.0, \n')
    f.write('    "angles" : "0.00000 0.00000 0.00000", \n')
    f.write('    "brightness" : 1.0, \n')
    f.write('    "color" : "1.00000 1.00000 1.00000", \n')
    f.write('    "colorBlendMode" : 0, \n')
    f.write('    "copybackground" : true, \n')
    f.write('    "id" :' + str(ID) + ', \n')
    f.write('    "image" : "models/' + str(i) + '.json", \n')
    f.write('    "ledsource" : false, \n')
    f.write('    "locktransforms" : false, \n')
    f.write('    "name" : "' + str(i) + '", \n')
    f.write('    "origin" : "540.00000 1170.00000 0.00000", \n')
    f.write('    "parallaxDepth" : "1.00000 1.00000", \n')
    f.write('    "perspective" : false, \n')
    f.write('    "scale" : "1.00000 1.00000 1.00000", \n')
    f.write('    "size" : "1080.00000 2340.00000", \n')
    f.write('    "solid" : true, \n')
    f.write('    "visible" : false \n')
    f.write('}, \n')

f.close()

### TEX JSON
for i in range(START, END + 1):
    f = open(MATERIALS_FOLDER +"/" + str(i) + ".tex-json", "w+")
    f.write('{ \n')
    f.write('    "bleedtransparentcolors" : true, \n')
    f.write('    "clampuvs" : true, \n')
    f.write('    "format" : "dxt1", \n')
    f.write('    "halfmip" : true, \n')
    f.write('    "nonpoweroftwo" : true \n')
    f.write('} \n')
    f.close()

### MATERIALS JSON
for i in range(START, END + 1):
    f = open(MATERIALS_FOLDER +"/" + str(i) + ".json", "w+")
    f.write('{ \n')
    f.write('    "passes" : \n')
    f.write('    [ \n')
    f.write('        { \n')
    f.write('            "blending" : "translucent", \n')
    f.write('            "combos" :  \n')
    f.write('            { \n')
    f.write('                "VERSION" : 2 \n')
    f.write('            }, \n')
    f.write('            "cullmode" : "nocull", \n')
    f.write('            "depthtest" : "disabled", \n')
    f.write('            "depthwrite" : "disabled", \n')
    f.write('            "shader" : "genericimage2", \n')
    f.write('            "textures" : [ "' + str(i) + '" ] \n')
    f.write('        } \n')
    f.write('    ] \n')
    f.write('} \n')
    f.close()

### MODELS JSON
for i in range(START, END + 1):
    f = open(MODELS_FOLDER +"/" + str(i) + ".json", "w+")
    f.write('{ \n')
    f.write('    "autosize" : true, \n')
    f.write('    "material" : "materials/' + str(i) + '.json" \n')
    f.write('} \n')
    f.close()