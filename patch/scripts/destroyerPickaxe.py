import random
from scripts.base import BaseScript
import autoit
import time


class DestroyerPickAxe(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "destroyerPickaxe"
        self.keyActivate = self.keys[self.name]
        self.attacks_count = 234  # 1866  933  467
        self.weapon_slot = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+0"] #
        self.started = False

    def master_action(self):
        if not self.started:
            self.started = True
            for key in self.weapon_slot:
                self.weapon_changer(key)
                self.attack_and_antiafk()
        self.jumping()

    def jumping(self):

        self.hold("space")
        self.wait(0.3)
        self.release("space")

        self.wait(1)
        print("jumping")

    def moving(self):
        self.hold_and_release("s", 1.4)
        time.sleep(0.5)
        self.hold_and_release("w", 1.4)
        time.sleep(0.5)
        self.hold_and_release("s", 1.4)
        time.sleep(0.5)
        self.hold_and_release("w", 1.6)
        time.sleep(0.5)

    def attack_loop(self):
        count = 0
        while self.attacks_count > count:
            if self.isStop or self.exitKey:
                break
            self.attacker()
            count += 1

    def attack_and_antiafk(self):

        for _ in range(8):
            self.wait(1.03)
            self.attack_loop()
            self.wait(1.03)
            self.moving()
            self.wait(1.03)

    def attacker(self):
        if not self.isStop and not self.exitKey:
            self.hold("q")
            time.sleep(0.46)  # 0.25
            print()
            self.release("q")

            time.sleep(0.55)
            print("attacker")

    def weapon_changer(self, key):
        self.wait(1)
        self.press(key)
        self.wait(2)
        self.press('x')
        self.wait(1)

    def customLoop(self):
        self.started = False
        while not self.exitKey and not self.isStop:
            self.custom()
            self.checkExitKey()
            self.checkStopKey()

    def custom(self):
        self.master_action()


def run():
    script_class = DestroyerPickAxe()
    script_class.custom()


if __name__ == "__main__":
    run()


