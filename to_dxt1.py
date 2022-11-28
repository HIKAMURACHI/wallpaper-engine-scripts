import os
import json

files = []

for file in os.listdir():
    if file.endswith(".tex-json"):
        files.append(os.path.join("", file))

print(len(files))

for i in files:
    print(i)
    with open(i, "rt", encoding="utf-8") as file:
        settings = json.load(file)
    
    settings["format"] = "dxt1"
    
    with open(i, "wt", encoding="utf-8") as file:
        json.dump(settings, file, indent=2)