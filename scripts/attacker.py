# СЕНСА НА 30%

import random
import time

import win32con

from scripts.base import BaseScript
import win32, win32api, win32gui


class Script(BaseScript):

    def __init__(self):
        super().__init__()
        self.name = "attacker"
        self.keys = self.keys_data[self.name][0]  # загрузка настройки всех ключей данного скрипта
        self.keyActivate = self.keys["activate_key"]  # кнопка активации скрипта
        self.ready = True if self.keys["activate_key"] != "" else False
        self.overhead = self.keys["key1"]["value"]
        self.right = self.keys["key2"]["value"]
        self.left = self.keys["key3"]["value"]
        self.down = self.keys["key4"]["value"]
        self.mode = self.keys["key5"]["value"]
        self.timing = float(self.keys["key6"]["value"])
        self.charging = float(self.keys["key7"]["value"])
        self.feint = self.keys["key8"]["value"]
        self.feint_bool = self.keys["key9"]["value"]
        self.rotation_bool = self.keys["key10"]["value"]
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
        self.test = None

    def feint_rotate_pierce_to_side(self):
        if self.rotation_bool == '1':
            time.sleep(0.8)
            x = 32
            y = 20
            time_count = 30

            after = 1
            self.hold(self.down)
            self.rotate(time_count-after, x, -int(y*2))
            self.press(self.feint)
            self.rotate(after, x, -int(y*2))
            self.release(self.down)
            before = 4
            self.rotate(before, x, 0)
            self.press(random.choice([self.left, self.right]))
            self.rotate(time_count-before, x, int(y/2))
            self.rotate(time_count, x, y)
            self.hold(self.left)
            self.rotate(time_count, -x, y)
            self.press(self.feint)
            before = 2
            self.rotate(before, -x, -int(y / 4))
            self.release(self.left)
            after = 17
            self.rotate(time_count-before-after, -x, -int(y/4))
            self.press(self.right)
            self.rotate(after, -x, -int(y / 4))
            self.rotate(time_count, -x, -int(y/2))


    def feint_rotate_look_down(self):
        if self.rotation_bool == '1':
            time.sleep(0.8)
            x = 33
            y = -20
            time_count = 28
            time_count_double = 56
            self.hold(self.overhead)
            sum_x = 0
            sum_y = 0
            for _ in range(time_count-2):
                sum_x += -x
                sum_y += -y
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, -y, 0, 0)
                time.sleep(0.01)
            self.press(self.feint)
            sum_x += -x
            sum_y += -y
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, -y, 0, 0)
            time.sleep(0.01)
            self.release(self.overhead)
            sum_x += -x
            sum_y += -y
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, 0, 0, 0)
            time.sleep(0.01)
            self.actually_attack = self.left
            for _ in range(int(time_count_double/4)):
                sum_x += -x
                sum_y += int(y/4)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, int(0), 0, 0)
                time.sleep(0.01)
            self.press(self.actually_attack)
            for _ in range(int(time_count_double/4)):
                sum_x += -x
                sum_y += int(y / 4)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, int(0), 0, 0)
                time.sleep(0.01)
            for _ in range(int(time_count_double/2)):
                sum_x += -x
                sum_y += int(y)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, int(y/1.5), 0, 0)
                time.sleep(0.01)

            self.actually_attack = self.right
            for _ in range(int(time_count_double/4)):
                sum_x += x
                sum_y += -int(y/4)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y/4), 0, 0)
                time.sleep(0.01)
            self.hold(self.overhead)
            for _ in range(int(time_count_double/4)):
                sum_x += x
                sum_y += -int(y / 4)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y/4), 0, 0)
                time.sleep(0.01)
            self.press(self.feint)
            self.release(self.overhead)
            for _ in range(int(time_count_double/4)):
                sum_x += x
                sum_y += -int(y)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, 0, 0, 0)
                time.sleep(0.01)
            self.press(self.actually_attack)
            for _ in range(int(time_count_double/4)):
                sum_x += x
                sum_y += -int(y)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y*2), 0, 0)
                time.sleep(0.01)
            for _ in range(time_count):
                sum_x += x
                sum_y += y
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
                time.sleep(0.01)

            print(f"SUMMA: x = {sum_x} , y = {sum_y} ")


    def feint_pierce_attack(self):
        if self.rotation_bool == '1':
            time.sleep(0.8)
            x = 32
            y = 20
            time_count = 20
            extra_time_count = 3

            for _ in range(extra_time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, 0, 0, 0)
                time.sleep(0.01)

            for _ in range(int(time_count)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -y, 0, 0)
                time.sleep(0.01)

            before = 7
            for _ in range(int(time_count-before)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -y, 0, 0)
                time.sleep(0.01)

            self.actually_attack = self.down
            self.press(self.actually_attack)

            for _ in range(int(before)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -y, 0, 0)
                time.sleep(0.01)

            for _ in range(time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, 0, 0, 0)
                time.sleep(0.01)

            for _ in range(time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, int(y*2), 0, 0)
                time.sleep(0.01)

            for _ in range(extra_time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, 0, 0, 0)
                time.sleep(0.01)
            time.sleep(0.1)


    def feint_rotate_and_jump(self):
        if self.rotation_bool == '1':
            time.sleep(0.8)
            x = 32
            y = 4
            time_count = 24
            sum_x = 0
            sum_y = 0
            self.hold(self.right)
            for _ in range(time_count-2):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, y, 0, 0)
                time.sleep(0.01)
                sum_x += -x
                sum_y += y
            self.press(self.feint)
            for _ in range(1):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, y, 0, 0)
                time.sleep(0.01)
                sum_x += -x
                sum_y += y
            self.hold("space")
            for _ in range(1):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, y, 0, 0)
                time.sleep(0.01)
                sum_x += -x
                sum_y += y
            self.actually_attack = random.choice([self.left, self.left, self.right])
            extra = 0
            if self.actually_attack == self.right:
                extra = 22
            self.press(self.actually_attack)
            for _ in range(time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, y-extra, 0, 0)
                time.sleep(0.01)
                sum_x += -x
                sum_y += y

            for _ in range(time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, y, 0, 0)
                time.sleep(0.01)
                sum_x += -x
                sum_y += y
            self.release("space")

            for _ in range(time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, y+extra, 0, 0)
                time.sleep(0.01)
                sum_x += -x
                sum_y += y
            self.hold("space")

            before = 8
            for _ in range(time_count-before):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y*5), 0, 0)
                time.sleep(0.01)
                sum_x += x
                sum_y += -int(y*3)




            for _ in range(time_count+before):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y*5), 0, 0)
                time.sleep(0.01)
                sum_x += x
                sum_y += -int(y*3)
            self.actually_attack = random.choice([self.right, self.overhead])
            self.press(self.actually_attack)
            for _ in range(time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, int(y), 0, 0)
                time.sleep(0.01)
                sum_x += x
                sum_y += int(y)
            for _ in range(time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, int(y*5), 0, 0)
                time.sleep(0.01)
                sum_x += x
                sum_y += int(y)

            print(f"SUMMA: x = {sum_x} , y = {sum_y} ")
            self.wait(0.1)

    def feint_look_down_left(self):
        time.sleep(0.5)
        if self.rotation_bool == '1':
            time.sleep(0.8)
            x = 32
            y = 15
            time_count = 60
            for _ in range(int(time_count/4)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, y, 0, 0)
                time.sleep(0.01)

            self.actually_attack = self.overhead
            self.press(self.actually_attack)
            for _ in range(int(time_count/4)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, y, 0, 0)
                time.sleep(0.01)

            for _ in range(int(time_count/2)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -y, 0, 0)
                time.sleep(0.01)
            time.sleep(0.2)

    def feint_look_down_right(self):
        time.sleep(0.5)
        if self.rotation_bool == '1':
            time.sleep(0.8)
            x = 32
            y = 15
            time_count = 60
            for _ in range(int(time_count/4)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
                time.sleep(0.01)

            self.actually_attack = self.overhead
            self.press(self.actually_attack)
            for _ in range(int(time_count/4)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
                time.sleep(0.01)

            for _ in range(int(time_count/2)):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, -y, 0, 0)
                time.sleep(0.01)
            time.sleep(0.2)

    def feint_double_strafe_attack(self):
        attack = random.choice([self.feint_left_attack, self.feint_right_attack])
        attack()
        self.feint_left_attack() if attack == self.feint_right_attack else self.feint_right_attack()


    def feint_left_attack(self):
        if self.rotation_bool == '1':

            x = 26
            y = 12
            time_count = 20

            self.rotate(time_count, x, y)
            after = 12
            self.rotate(time_count-after, x, y)

            self.actually_attack = self.left
            self.press(self.actually_attack)
            self.rotate(after, x, y)

            self.rotate(time_count, -x, -y)
            self.rotate(time_count, -x, -y)
            time.sleep(0.01)

    def feint_right_attack(self):
        if self.rotation_bool == '1':

            x = 32
            y = 12
            time_count = 20

            self.rotate(time_count, -x, y)
            after = 12
            self.rotate(time_count-after, -x, y)

            self.actually_attack = self.right
            self.press(self.actually_attack)
            self.rotate(after, -x, y)

            self.rotate(time_count, x, -y)
            self.rotate(time_count, x, -y)
            time.sleep(0.01)

    def feint_rotate_90(self):
        if self.rotation_bool == '1':
            time.sleep(0.8)
            x = 32
            y = 20
            time_count = 40
            self.hold(self.overhead)
            for _ in range(time_count-14):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, -y, 0, 0)
                time.sleep(0.01)
            self.press(self.feint)
            self.rotate(1, -x, -y)
            self.release(self.overhead)
            self.rotate(3, -x, -y)
            self.actually_attack = self.right
            self.press(self.actually_attack)
            self.rotate(10, -x, -y)
            for _ in range(time_count):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
                time.sleep(0.01)

    def feint_rotate(self):
        if self.rotation_bool == '1':
            time.sleep(0.8)
            x = 33
            y = 20
            time_count = 28
            time_count_double = 56
            self.hold(self.overhead)
            sum_x = 0
            sum_y = 0
            for _ in range(time_count):
                sum_x += -x
                sum_y += -y
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, -y, 0, 0)
                time.sleep(0.01)
            self.press(self.feint)
            self.rotate(1, -x, int(y/4))
            self.release(self.overhead)
            self.rotate(1, -x, int(y / 4))
            self.actually_attack = self.left

            for _ in range(int((time_count_double/4)-2)):
                sum_x += -x
                sum_y += int(y/4)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, int(y/4), 0, 0)
                time.sleep(0.01)
            self.press(self.actually_attack)
            for _ in range(int(time_count_double/4)):
                sum_x += -x
                sum_y += int(y / 4)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, int(y/4), 0, 0)
                time.sleep(0.01)
            for _ in range(int(time_count_double/2)):
                sum_x += -x
                sum_y += int(y)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -x, int(y), 0, 0)
                time.sleep(0.01)

            self.actually_attack = self.right
            for _ in range(int(time_count_double/4)):
                sum_x += x
                sum_y += -int(y/4)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y/4), 0, 0)
                time.sleep(0.01)
            self.hold(self.overhead)
            for _ in range(int((time_count_double/4)-2)):
                sum_x += x
                sum_y += -int(y / 4)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y/4), 0, 0)
                time.sleep(0.01)
            self.press(self.feint)
            self.rotate(1, x, -int(y/4))
            self.release(self.overhead)

            self.rotate(1, x, -int(y / 4))
            self.hold(self.overhead)
            for _ in range(int(time_count_double/4)):
                sum_x += x
                sum_y += -int(y)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y), 0, 0)
                time.sleep(0.01)
            self.press(self.feint)
            self.rotate(4, x, -int(y))
            self.release(self.overhead)

            self.rotate(4, x, y)
            self.press(self.actually_attack)
            for _ in range(int((time_count_double/4)-4)):
                sum_x += x
                sum_y += -int(y)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, -int(y), 0, 0)
                time.sleep(0.01)
            for _ in range(time_count-4):
                sum_x += x
                sum_y += y
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
                time.sleep(0.01)

            print(f"SUMMA: x = {sum_x} , y = {sum_y} ")

    def feint_deep_random_to_random(self):
        last_attack = None
        for _ in range(random.choice([2, 3, 4, 3, 4, 5, 6])):
            self.choose_attack()
            while last_attack == self.actually_attack:
                self.choose_attack()
            self.hold(self.actually_attack)
            self.wait(0.2)
            self.press(self.feint)
            self.release(self.actually_attack)
            self.wait(0.01)
            last_attack = self.actually_attack

        attack = random.choice(self.move_keys)
        if attack == self.side_attack:
            attack = random.choice(self.side_attack)
        self.press(attack)

    def choose_attack(self):
        self.actually_attack = random.choice(self.move_keys)
        if self.actually_attack == self.side_attack:
            self.actually_attack = random.choice(self.side_attack)
        self.debug_log(f"self.actually_attack = {self.actually_attack}")

    def feint_random_to_random(self):
        self.choose_attack()
        self.hold(self.actually_attack)
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

    def rotate(self, time_count, x_speed, y_speed, func=None):
        sum_x = 0
        sum_y = 0
        for _ in range(time_count):
            sum_x += x_speed
            sum_y += y_speed
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x_speed, y_speed, 0, 0)
            time.sleep(0.01)
            if func is not None:
                func()

    def feints_attacks(self):
        random.choice([self.attacks,
                       self.attacks,
                       random.choice([self.feint_side_to_over,
                                      self.feint_random_to_random,
                                      self.feint_over_to_side,
                                      self.feint_deep_random_to_random,
                                      self.feint_deep_random_to_random,
                                      self.feint_rotate_90,
                                      self.feint_rotate,
                                      self.feint_right_attack,
                                      self.feint_look_down_right,
                                      self.feint_look_down_left,
                                      self.feint_rotate_and_jump,
                                      self.feint_pierce_attack,
                                      self.feint_rotate_look_down,
                                      self.feint_rotate_pierce_to_side
                                      ])])()

    def custom(self):
        # Тестовый финт. None, если нет теста
        test = self.test

        if test is not None:
            test()
            self.wait(2)
        else:
            if self.feint_bool == "1":
                self.feints_attacks()
            else:
                self.attacks()


def run():
    script_class = Script()
    script_class.custom()


if __name__ == "__main__":
    run()
