import autoit
import keyboard
import mouse
import pyautogui

from scripts.base import BaseScript


class Script(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "easyFlux"
        self.keys = self.keys_data[self.name][0]
        self.keyActivate = self.keys["activate_key"]
        self.expel = self.keys["key1"]["value"]
        self.call_spirits = self.keys["key2"]["value"]
        self.attack_key = self.keys["key3"]["value"]
        self.holding_left = False
        self.timer = 0
        self.toggle = False
        self.first = False
        self.ready = False
        pyautogui.FAILSAFE = False

    def custom(self):

        self.wait(0.01)
        self.timer += 0.01

        if mouse.is_pressed(button="right") and self.timer > 0.5:
            if not self.holding_left:
                self.holding_left = True
                self.hold("g")
                self.timer = 0
            else:
                self.holding_left = False
                self.release("g")
                self.timer = 0

        if keyboard.is_pressed("1"):
            self.press("3")
            self.hold_and_release_sleep("w", 0.2)
            self.wait(0.1)
            self.press('k')
        if keyboard.is_pressed("2"):
            self.press("4")
            self.hold_and_release_sleep("w", 0.1)
            self.wait(0.1)
            self.press('k')

def run():
    attack_spam = Script()
    attack_spam.custom()


if __name__ == "__main__":
    run()
