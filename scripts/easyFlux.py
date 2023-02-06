import autoit
import keyboard
import mouse
import pyautogui

from scripts.base import BaseScript


class EasyFlux(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "easyFlux"
        self.keys = self.keys_data[self.name]
        self.keyActivate = self.keys["activate_key"]
        self.holding_left = False
        self.timer = 0
        self.toggle = False
        self.first = False
        pyautogui.FAILSAFE = False

    def custom(self):
        speed = 1
        if keyboard.is_pressed('f4') and not self.first:
            pyautogui.press('escape')
            autoit.mouse_click("left", speed=speed, x=961, y=420)
            autoit.mouse_click("left", speed=speed, x=730, y=737)
            autoit.mouse_click("left", speed=speed, x=647, y=797)
            autoit.mouse_click("left", speed=speed, x=720, y=610)
            autoit.mouse_click("left", speed=speed, x=680, y=730)  # autoit.mouse_click("left", x=680, y=710)
            autoit.mouse_click("left", speed=speed, x=820, y=980)
            self.toggle = True
            self.first = True
            self.wait(0.3)

        elif keyboard.is_pressed('f4') and not self.toggle:
            pyautogui.press('escape')
            autoit.mouse_click("left", speed=speed, x=961, y=420)
            autoit.mouse_click("left", speed=speed, x=720, y=610)
            autoit.mouse_click("left", speed=speed, x=680, y=730)  # autoit.mouse_click("left", x=680, y=710)
            autoit.mouse_click("left", speed=speed, x=820, y=980)
            self.toggle = True
            self.wait(0.3)
        elif keyboard.is_pressed('f4') and self.toggle:
            pyautogui.press('escape')
            autoit.mouse_click("left", speed=speed, x=961, y=420)
            autoit.mouse_click("left", speed=speed, x=720, y=610)
            autoit.mouse_click("left", speed=speed, x=680, y=640)  #
            autoit.mouse_click("left", speed=speed, x=820, y=980)
            self.toggle = False
            self.wait(0.3)

        # self.wait(0.01)
        # self.timer += 0.01
        #
        #
        # if mouse.is_pressed(button="right") and self.timer > 0.5:
        #     if not self.holding_left:
        #         self.holding_left = True
        #         self.hold("g")
        #         self.timer = 0
        #     else:
        #         self.holding_left = False
        #         self.release("g")
        #         self.timer = 0
        #
        # if keyboard.is_pressed("1"):
        #     self.press("3")
        #     self.hold_and_release_sleep("w", 0.2)
        #     self.wait(0.1)
        #     self.press('k')
        # if keyboard.is_pressed("2"):
        #     self.press("4")
        #     self.hold_and_release_sleep("w", 0.1)
        #     self.wait(0.1)
        #     self.press('k')

def run():
    attack_spam = EasyFlux()
    attack_spam.custom()


if __name__ == "__main__":
    run()
