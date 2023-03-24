import json

def readJson(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def writeJson(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)

