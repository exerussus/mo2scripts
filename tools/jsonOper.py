import json
import os


def onlySaveKeys(keys):

    keys_data = json.dumps(keys)
    with open("data/keys.json", "w") as file:
        file.write(keys_data)


def standard_keys(script_name: str):
    result = {}
    exec(f"import scripts.{script_name}")
    script_class = eval(f"scripts.{script_name}.Script")
    result[script_class.name] = script_class.config
    return result


def get_scripts_dict():
    result = {}
    for filename in os.listdir("scripts"):
        if filename[-2:] == "py":
            filename = filename[:-3]
            if filename != "base" and filename != "NewScriptSample":
                exec(f"import scripts.{filename}")

                script_class = eval(f"scripts.{filename}.Script")
                result[script_class.name] = script_class.config
    return result

def get_description(script_name: str):
    exec(f"import scripts.{script_name}")
    script_class = eval(f"scripts.{script_name}.Script")
    return script_class.description

def reset_all():
    result = get_scripts_dict()
    keys_data = json.dumps(result)
    with open("data/keys.json", "w") as file:
        file.write(keys_data)


def saveKeysMainMod(keys):

    keys_data = json.dumps(keys)
    with open("../data/keys.json", "w") as file:
        file.write(keys_data)

def saveKeys(keys):

    keys_data = json.dumps(keys)
    with open("data/keys.json", "w") as file:
        file.write(keys_data)


def onlyLoadKeys():
    with open("../data/keys.json", "r") as file:
        keys_data = file.read()

    return json.loads(keys_data)


def loadKeys(name: str):
    with open("data/keys.json", "r") as file:
        keys_data = file.read()

    return json.loads(keys_data)[name]


def loadKeysGuiMainMod():
    with open("../data/keys.json", "r") as file:
        keys_data = file.read()

    return json.loads(keys_data)


def loadKeysGui():
    with open("data/keys.json", "r") as file:
        keys_data = file.read()

    return json.loads(keys_data)





