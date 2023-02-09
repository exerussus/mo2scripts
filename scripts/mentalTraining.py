import random
from scripts.base import BaseScript
import pyautogui

class Script(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "mentalTraining"
        self.keys = self.keys_data[self.name][0]
        self.keyActivate = self.keys["activate_key"]
        self.ready = False

    def water_pushing(self):

        self.press("k")
        self.wait(2)
        self.press("k")
        self.wait(0.7)

    def water_pushing_x5(self):

        self.water_pushing()
        self.water_pushing()
        self.water_pushing()
        self.water_pushing()
        self.water_pushing()

    def custom(self):

        self.wait(1.3)
        self.func_repetition(self.water_pushing, 15)
        self.press("0")
        self.wait(50)





def run():
    script_class = Script()
    script_class.custom()


if __name__ == "__main__":
    run()
