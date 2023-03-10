import random
from scripts.base import BaseScript
import pyautogui

class Script(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "mentalTraining"
        self.keys = self.keys_data[self.name][0]
        self.keyActivate = self.keys["activate_key"]
        self.ready = True if self.keys["activate_key"] != "" else False
        self.spurt_key = self.keys["key1"]["value"]
        self.spurt_count = int(self.keys["key2"]["value"])
        self.healing_key = self.keys["key3"]["value"]
        self.healing_count = self.keys["key4"]["value"]
        self.resting_key = self.keys["key5"]["value"]
        self.resting_time = float(self.keys["key6"]["value"])
        self.self_cast = self.keys["key7"]["value"]
        if self.healing_count != "" and self.healing_key != "":
            self.healing_count = int(self.healing_count)

        self.ready = True

    def water_pushing(self):

        self.press(self.spurt_key)
        self.wait(2)
        self.press(self.self_cast)
        self.wait(0.7)

    def healing(self):
        if self.healing_count != "" and self.healing_key != "":
            self.press(self.healing_key)
            self.wait(2)
            self.press(self.self_cast)
            self.wait(0.7)

    def custom(self):

        self.wait(1.3)
        self.func_repetition(self.water_pushing, self.spurt_count)
        self.func_repetition(self.healing, self.healing_count)
        self.press(self.resting_key)
        self.wait(self.resting_time)


def run():
    script_class = Script()
    script_class.custom()


if __name__ == "__main__":
    run()
