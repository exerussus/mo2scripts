import os

from scripts.base import BaseScript
import tools.jsonOper


class Script(BaseScript):

    name = file_name = os.path.basename(__file__)[:-3]
    config = {
        "activate_key": "f5",
        "key1": {"name": "1. Кнопка нажатия", "value": ""},
        "key2": {"name": "1. Пауза после нажатия", "value": ""},

        "key3": {"name": "2. Кнопка зажатия", "value": ""},
        "key4": {"name": "2. Время зажатия", "value": ""},

        "key5": {"name": "1-2. Количество повторений", "value": ""},

        "key6": {"name": "3. Кнопка нажатия", "value": ""},
        "key7": {"name": "3. Пауза после нажатия", "value": ""},

        "key8": {"name": "4. Кнопка зажатия", "value": ""},
        "key9": {"name": "4. Время зажатия", "value": ""},

        "key10": {"name": "3-4. Количество повторений", "value": ""},
    }
    description = ""
    keys = tools.jsonOper.loadKeys(name)
    ready = True if keys["activate_key"] != "" else False

    def __init__(self):
        super().__init__()
        self.name = Script.name
        self.keys = Script.keys
        self.keyActivate = self.keys["activate_key"]
        self.press_1 = self.keys["key1"]["value"]
        self.wait_1 = self.keys["key2"]["value"]
        self.hold_2 = self.keys["key3"]["value"]
        self.holding_time_2 = self.keys["key4"]["value"]
        self.cycle12 = self.keys["key5"]["value"]
        self.press_3 = self.keys["key6"]["value"]
        self.wait_3 = self.keys["key7"]["value"]
        self.hold_4 = self.keys["key8"]["value"]
        self.holding_time_4 = self.keys["key9"]["value"]
        self.cycle34 = self.keys["key10"]["value"]

    def custom(self):
        for _ in range(int(self.cycle12) if self.cycle12 != "" else 1):
            if self.press_1 != "":
                self.press(self.press_1)
            if self.wait_1 != "":
                self.wait(float(self.wait_1))

            if self.hold_2 != "":
                self.hold_and_release_wait(self.hold_2, float(self.holding_time_2))

        for _ in range(int(self.cycle34) if self.cycle34 != "" else 1):
            if self.press_3 != "":
                self.press(self.press_3)
            if self.wait_3 != "":
                self.wait(float(self.wait_3))

            if self.hold_4 != "":
                self.hold_and_release_wait(self.hold_4, float(self.holding_time_4))
        # self.hold_and_release_wait('w', 1)
        # self.hold_and_release_wait('space', 1)
        # self.hold_and_release_wait('s', 1)
        # self.hold_and_release_wait('space', 1)

def run():
    attack_spam = Script()
    attack_spam.custom()


if __name__ == "__main__":
    run()
