import json

#
# def saveKeys(keys):
#     with open("../data/keys.json", "w") as file:
#         json.dump(keys, file)
#
#
# def loadKeys():
#     with open("../data/keys.json", "r") as file:
#         json.load(file)

dct = {"domination": "f4",
       "base": "",
       "attackspam": "f5",
       "attacker": "f3",
       "feintRightAttackOverhead": "f",
       "spacer": "f2",
       "mentalTraining": "f1",
       "destroyerPickaxe": "f6",
       "destroyerDagger": "f8"}



def saveKeys(keys):
    dct = keys


def loadKeys():
    return dct
