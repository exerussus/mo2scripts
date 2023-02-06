import autoit
import keyboard
import mouse
import pyautogui
import time
from scripts.base import BaseScript


class intBoost(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "intBoost"
        self.keys = self.keys_data[self.name]
        self.keyActivate = self.keys["activate_key"]
        self.holding_left = False
        self.timer = 0
        self.toggle = False
        self.first = False
        self.loop = False
        pyautogui.FAILSAFE = False

    def custom(self):

        speed = 1
        time.sleep(2)
        while not self.isStop and not self.exitKey:
            self.hold('lshift')
            self.wait(0.1)
            self.hold('lshift')
            autoit.mouse_click("right", speed=speed, x=1670, y=1000)
            self.wait(0.1)

            self.release('lshift')
            self.wait(0.1)
            self.press('1')
            self.wait(0.05)

            autoit.mouse_click("left", speed=speed, x=1720, y=1050)

            self.wait(0.05)
            autoit.mouse_click("right", speed=speed, x=1750, y=1030)
            autoit.mouse_move(speed=speed, x=960, y=630)
            self.wait(0.05)

            autoit.mouse_down("left")
            self.wait(1.45)
            autoit.mouse_up("left")
            self.wait(0.1)
            self.release('lshift')









def run():
    attack_spam = intBoost()
    attack_spam.custom()


if __name__ == "__main__":
    run()
