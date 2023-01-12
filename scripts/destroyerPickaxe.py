import random
from scripts.base import BaseScript
import autoit

class DestroyerPickAxe(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "destroyerPickaxe"
        self.keyActivate = self.keys[self.name]
        self.attacks_count = 933  # 1866  933
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
        # if not self.isStop and not self.exitKey:
        #     autoit.control_send(f"[TITLE:{self.game}]", "", "{space down}")
        self.hold("space")
        self.wait(0.3)
        self.release("space")
        # if not self.isStop and not self.exitKey:
        #     autoit.control_send(f"[TITLE:{self.game}]", "", "{space up}")
        self.wait(1)
        print("jumping")

    def moving(self):
        self.hold('s')
        self.wait(1)
        self.release("s")
        self.wait(1)
        self.hold('w')
        self.wait(1)
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
        self.wait(0.29)  # 0.25
        print()
        self.release("q")
        print("attacker")
        self.wait(0.55)
        print()


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


