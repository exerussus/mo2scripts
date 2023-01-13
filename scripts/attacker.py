import random
from scripts.base import BaseScript
import pyautogui


class Attacker(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "attacker"
        self.keyActivate = self.keys[self.name]
        # self.move_keys = ["q", "{alt}", "v", "k"]

    def custom(self):
        # with pyautogui.hold("left"):
        #     self.press(random.choice(self.move_keys))
        #     self.wait(0.3)
        with pyautogui.hold("q"):
            self.wait(0.25)  # 0.28
            print()


def run():
    script_class = Attacker()
    script_class.custom()


if __name__ == "__main__":
    run()
