import autoit
import keyboard
import mouse
import pyautogui
import time
from scripts.base import BaseScript


class Script(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "intBoost"
        self.keys = self.keys_data[self.name][0]
        self.keyActivate = self.keys["activate_key"]
        self.window_w = int(self.keys["key2"]["value"])
        self.window_h = int(self.keys["key3"]["value"])
        self.holding_left = False
        self.timer = 0
        self.toggle = False
        self.first = False
        self.loop = False
        self.ready = True if self.keys["activate_key"] != "" else False

    def clc_x(self, x):
        return round(x/1920 * self.window_w)

    def clc_y(self, y):
        return round(y/1080 * self.window_h)

    def custom(self):

        speed = 1
        time.sleep(2)
        while not self.isStop and not self.exitKey:
            self.hold('lshift')
            self.wait(0.1)
            self.hold('lshift')
            autoit.mouse_click("right", speed=speed, x=self.clc_x(1670), y=self.clc_y(1000))
            self.wait(0.1)

            self.release('lshift')
            self.wait(0.1)
            self.press('1')
            self.wait(0.05)

            autoit.mouse_click("left", speed=speed, x=self.clc_x(1720), y=self.clc_y(1050))

            self.wait(0.05)
            autoit.mouse_click("right", speed=speed, x=self.clc_x(1750), y=self.clc_y(1030))
            autoit.mouse_move(speed=speed, x=self.clc_x(960), y=self.clc_y(630))
            self.wait(0.05)

            autoit.mouse_down("left")
            self.wait(1.45)
            autoit.mouse_up("left")
            self.wait(0.1)
            self.release('lshift')









def run():
    attack_spam = Script()
    attack_spam.custom()


if __name__ == "__main__":
    run()
