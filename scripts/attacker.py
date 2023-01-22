import random
from scripts.base import BaseScript
import pyautogui


class Attacker(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "attacker"
        self.keys = self.keys_data[self.name]  # загрузка настройки всех ключей данного скрипта
        self.keyActivate = self.keys["activate_key"]  # кнопка активации скрипта
        self.overhead = self.keys["key1"]["value"]
        self.right = self.keys["key2"]["value"]
        self.left = self.keys["key3"]["value"]
        self.down = self.keys["key4"]["value"]
        self.mode = self.keys["key5"]["value"]
        self.timing = float(self.keys["key6"]["value"])
        self.charging = float(self.keys["key7"]["value"])
        self.feint = self.keys["key8"]["value"]
        self.feint_bool = self.keys["key9"]["value"]

        self.side_attack = []
        self.move_keys = []
        self.actually_attack = None
        match self.mode:
            case '1':
                self.side_attack = [self.left]
                self.move_keys = [self.overhead, self.down, self.side_attack]
            case '2':
                self.side_attack = [self.right]
                self.move_keys = [self.overhead, self.down, self.side_attack]
            case '3':
                self.move_keys = [self.down]
            case '4':
                self.move_keys = [self.overhead, self.down]
            case '5':
                self.side_attack = [self.left, self.right]
                self.move_keys = [self.overhead, self.down, self.side_attack]

    def feint_deep_random_to_random(self):
        for _ in range(random.choice([2, 3, 4, 3, 4, 5])):
            self.choose_attack()

            self.hold(self.actually_attack)
            self.wait(0.2)
            self.press(self.feint)
            self.release(self.actually_attack)
            self.wait(0.01)

        attack = random.choice(self.move_keys)
        if attack == self.side_attack:
            attack = random.choice(self.side_attack)
        self.press(attack)

    def choose_attack(self):
        self.actually_attack = random.choice(self.move_keys)
        if self.actually_attack == self.side_attack:
            self.actually_attack = random.choice(self.side_attack)

    def feint_random_to_random(self):
        self.choose_attack()

        self.hold(self.actually_attack)
        self.wait(0.2)
        self.press(self.feint)
        self.release(self.actually_attack)
        self.wait(0.01)

        self.choose_attack()
        self.press(self.actually_attack)

    def feint_over_to_side(self):
        side_attack = random.choice(self.side_attack)
        self.hold(self.overhead)
        self.wait(0.3)
        self.press(self.feint)
        self.release(self.overhead)
        self.wait(0.02)
        self.press(side_attack)
        self.wait(0.01)

    def feint_side_to_over(self):
        side_attack = random.choice(self.side_attack)
        self.hold(side_attack)
        self.wait(0.2)
        self.press(self.feint)
        self.release(side_attack)
        self.wait(0.01)
        self.press(self.overhead)

    def attacks(self):
        self.choose_attack()

        if self.actually_attack == self.down:
            self.choose_attack()

        self.hold_and_release_wait(self.actually_attack, self.charging)
        self.wait(self.timing)

    def feints_attacks(self):
        rnd = random.choice([1, 2, 3])
        if rnd != 1:
            self.attacks()
        else:
            random.choice([self.feint_side_to_over,
                           self.feint_random_to_random,
                           self.feint_over_to_side,
                           self.feint_deep_random_to_random])()

    def custom(self):
        if self.feint_bool == "1":
            self.feints_attacks()
        else:
            self.attacks()


def run():
    script_class = Attacker()
    script_class.custom()


if __name__ == "__main__":
    run()
