import json


def onlySaveKeys(keys):

    keys_data = json.dumps(keys)
    with open("../data/keys.json", "w") as file:
        file.write(keys_data)


def reset():
    keys_data = json.dumps(dct)
    with open("data/keys.json", "w") as file:
        file.write(keys_data)


def saveKeys(keys):

    keys_data = json.dumps(keys)
    with open("data/keys.json", "w") as file:
        file.write(keys_data)


def loadKeys():
    with open("data/keys.json", "r") as file:
        keys_data = file.read()

    return json.loads(keys_data)


dct = {"domination": {
                        "activate_key": "f4",
                        "key1": {"name": "", "value": ""},
                        "key2": {"name": "", "value": ""},
                        "key3": {"name": "", "value": ""},
                        "key4": {"name": "", "value": ""},
                        "key5": {"name": "", "value": ""},
                        "key6": {"name": "", "value": ""},
                    },
       "base": {
                        "activate_key": "",
                        "key1": {"name": "", "value": ""},
                        "key2": {"name": "", "value": ""},
                        "key3": {"name": "", "value": ""},
                        "key4": {"name": "", "value": ""},
                        "key5": {"name": "", "value": ""},
                        "key6": {"name": "", "value": ""},
                    },
       "attackspam": {
                        "activate_key": "f5",
                        "key1": {"name": "", "value": ""},
                        "key2": {"name": "", "value": ""},
                        "key3": {"name": "", "value": ""},
                        "key4": {"name": "", "value": ""},
                        "key5": {"name": "", "value": ""},
                        "key6": {"name": "", "value": ""},
                    },
       "attacker": {
                        "activate_key": "f3",
                        "key1": {"name": "", "value": ""},
                        "key2": {"name": "", "value": ""},
                        "key3": {"name": "", "value": ""},
                        "key4": {"name": "", "value": ""},
                        "key5": {"name": "", "value": ""},
                        "key6": {"name": "", "value": ""},
                    },
       "spacer": {
                        "activate_key": "f2",
                        "key1": {"name": "", "value": ""},
                        "key2": {"name": "", "value": ""},
                        "key3": {"name": "", "value": ""},
                        "key4": {"name": "", "value": ""},
                        "key5": {"name": "", "value": ""},
                        "key6": {"name": "", "value": ""},
                    },
       "mentalTraining": {
                        "activate_key": "f1",
                        "key1": {"name": "", "value": ""},
                        "key2": {"name": "", "value": ""},
                        "key3": {"name": "", "value": ""},
                        "key4": {"name": "", "value": ""},
                        "key5": {"name": "", "value": ""},
                        "key6": {"name": "", "value": ""},
                    },
       "destroyerPickaxe": {
                        "activate_key": "f6",
                        "key1": {"name": "Атака сверху", "value": "q"},  # атака сверху
                        "key2": {"name": "Вытащить оружие", "value": "x"},  # вытащить оружие
                        "key3": {"name": "Прыжок", "value": "space"},  # прыжок
                        "key4": {"name": "Вперёд", "value": "w"},  # вперёд
                        "key5": {"name": "Назад", "value": "s"},  # назад
                        "key6": {"name": "Зарядка удара", "value": "0.295"},  # зарядка удара
                        "key7": {"name": "Отмашка", "value": "0.55"},  # отмашка
                        "key8": {"name": "Время ходьбы назад", "value": "3"},  # время ходьбы назад
                        "key9": {"name": "Время ходьбы вперёд", "value": "3.1"},  # время ходьбы вперёд

                        "key10": {"name": "Прочность", "value": "250"},  # Прочность
                        "key11": {"name": "Трата прочки за удар", "value": "0.14"},  # Трата прочности за удар

                        "key12": {"name": "1 доп. ячейка", "value": "t"},  #
                        "key13": {"name": "2 доп. ячейка", "value": "g"},  #
                        "key14": {"name": "3 доп. ячейка", "value": "b"},  #
                        "key15": {"name": "4 доп. ячейка", "value": "y"},  #
                        "key16": {"name": "5 доп. ячейка", "value": "h"},  #
                        "key17": {"name": "6 доп. ячейка", "value": "n"},  #
                        "key18": {"name": "7 доп. ячейка", "value": "u"},  #
                        "key19": {"name": "8 доп. ячейка", "value": "j"},  #
                        "key20": {"name": "9 доп. ячейка", "value": "m"},  #
                    },
       }


if __name__ == "__main__":
    onlySaveKeys(dct)
    # print(loadKeys())

