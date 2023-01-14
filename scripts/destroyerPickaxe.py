import random
from scripts.base import BaseScript
import autoit
import time


class DestroyerPickAxe(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "destroyerPickaxe"
        self.keys = self.keys_data[self.name]
        self.keyActivate = self.keys["activate_key"]

        self.attacks_count = 234  # 1866  933  467  234
        self.weapon_slot = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+0"] #
        self.started = False
        self.attack_overhead = self.keys["key1"]["value"]
        self.take_weapon = self.keys["key2"]["value"]
        self.jump_key = self.keys["key3"]["value"]
        self.key_forward = self.keys["key4"]["value"]
        self.key_backward = self.keys["key5"]["value"]
        self.hold_attack_time = float(self.keys["key6"]["value"])
        self.after_attack_time = float(self.keys["key7"]["value"])
        self.backward_walking_time = float(self.keys["key8"]["value"])
        self.forward_walking_time = float(self.keys["key9"]["value"])

    def master_action(self):
        if not self.started:
            self.started = True
            for key in self.weapon_slot:
                self.weapon_changer(key)
                self.attack_and_antiafk()
        self.jumping()

    def jumping(self):
        self.hold_and_release_wait(self.jump_key, 0.3)
        self.wait(1)
        print("jumping")

    def moving(self):
        self.hold_and_release_wait(self.key_backward, self.backward_walking_time)
        self.wait(0.5)
        self.jumping()
        self.wait(0.5)
        self.hold_and_release_wait(self.key_forward, self.forward_walking_time)
        self.wait(0.5)
        self.hold_and_release_wait(self.key_backward, self.backward_walking_time)
        self.wait(0.5)
        self.jumping()
        self.wait(0.5)
        self.hold_and_release_wait(self.key_forward, self.forward_walking_time)
        self.wait(0.5)

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
            self.hold_and_release_wait(self.attack_overhead, self.hold_attack_time)
            time.sleep(self.after_attack_time)
            print("attacker")
            print(self.keyActivate)
            print(self.attack_overhead)

    def weapon_changer(self, key):
        self.wait(1)
        self.press(key)
        self.wait(2)
        self.press(self.take_weapon)
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


