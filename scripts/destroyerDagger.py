import random
from scripts.base import BaseScript
import time


class DestroyerDagger(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "destroyerDagger"
        self.keyActivate = self.keys[self.name]
        self.attacks_count = 147  #  147
        self.weapon_slot = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+0"]
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
        self.hold('s')
        time.sleep(1)
        self.release("s")
        self.wait(1.03)
        self.hold('w')
        time.sleep(1)
        self.release("w")
        self.wait(1.03)

    def attack_and_antiafk(self):

        self.wait(1.03)
        count = 0
        while self.attacks_count > count:
            self.attacker()
            count += 1

        self.moving()

        count = 0
        while self.attacks_count > count:
            self.attacker()
            count += 1

        self.wait(0.5)

    def attacker(self):
        self.hold("q")
        time.sleep(0.49)  # Зарядка удара
        print()
        self.release("q")
        time.sleep(0.35)  # Отмашка
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
    script_class = DestroyerDagger()
    script_class.custom()


if __name__ == "__main__":
    run()


