import json


# LoadData takes a path to a file in the form of a string and attempts
# to load it as json. The resulting dictionary is returned.
def LoadData(path):
    jsonFileHandle = open(path)
    jsonStr = jsonFileHandle.read()
    try:
        jsonDataStruct = json.loads(jsonStr)
    except:
        print("Error loading menu json file, this will probably lead to a fatal error.")
        return nil
    return jsonDataStruct
