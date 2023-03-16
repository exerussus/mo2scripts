import os

import keyboard
import pyautogui
import ctypes

from scripts.base import BaseScript  # обязательный импорт для наследования
import tools.jsonOper


class Script(BaseScript):  # Название класса (должен отличаться от других названий скриптов)

    name = file_name = os.path.basename(__file__)[:-3]
    config = {
        "activate_key": "",
        "key1": {"name": "Клавиша назначения", "value": "q"},
        "key2": {"name": "Клавиша отдыха", "value": "0"},
        "key3": {"name": "Повторное нажатие для каста 1/0", "value": "1"},
        "key4": {"name": "Включить движение 1/0", "value": "1"},
        "key5": {"name": "Время каста 1", "value": "4"},
        "key6": {"name": "Время каста 2", "value": "1"},
        "key7": {"name": "Время каста 3", "value": "1"},
        "key8": {"name": "Время каста 4", "value": "1"},
        "key9": {"name": "Время каста 5", "value": "1"},
        "key10": {"name": "Время каста 6", "value": "1"},
        "key11": {"name": "Время каста 7", "value": "1"},
        "key12": {"name": "Время каста 8", "value": "1"},
        "key13": {"name": "Время каста 9", "value": "1"},
    }
    description = "После запуска скрипта, надо навести мышь\n" \
                  "на ячейку инвентаря и нажать клавишу назначения.\n" \
                  "После этого наведите на ячейку в банке и нажмите\n" \
                  "клавишу назначение. Так же\n" \
                  "нажмите ещё раз клавишу активации.\n"
    russian = 'Бесплатная прокачка'
    keys = tools.jsonOper.loadKeys(name)
    ready = True if keys["activate_key"] != "" else False

    def __init__(self):
        super().__init__()  # инициализация класса после наследования

        """                   Ключи - Обязательное                   """

        self.name = Script.name  # имя в базе ключей
        self.keys = Script.keys  # загрузка настройки всех ключей данного скрипта
        self.keyActivate = self.keys["activate_key"]  # кнопка активации скрипта
        # обязательно скопировать ключ-значение "base", и переименовать согласно значению в self.name

        """ Полезное, но имеющее значение по дефолту, удалить при ненадобности """
        self.game = "Mortal Online 2  "
        self.loop = True  # True активирует бесконечный цикл метода custom()
        self.debug = True  # Логи на стандартные функции
        self.window_w = 1920  # Ширина экрана (лучше настраивать через ключи)
        self.window_h = 1080  # Высота экрана (лучше настраивать через ключи)

        """ Кастомные атрибуты писать здесь """
        self.set_position_key = self.keys["key1"]["value"]
        self.rest_key = self.keys["key2"]["value"]
        self.cast_twice = True if self.keys["key3"]["value"] == "1" else False
        self.moving_mode = True if self.keys["key4"]["value"] == "1" else False
        self.cast_time_1 = float(self.keys["key5"]["value"])
        self.cast_time_2 = float(self.keys["key6"]["value"])
        self.cast_time_3 = float(self.keys["key7"]["value"])
        self.cast_time_4 = float(self.keys["key8"]["value"])
        self.cast_time_5 = float(self.keys["key9"]["value"])
        self.cast_time_6 = float(self.keys["key10"]["value"])
        self.cast_time_7 = float(self.keys["key11"]["value"])
        self.cast_time_8 = float(self.keys["key12"]["value"])
        self.cast_time_9 = float(self.keys["key13"]["value"])
        self.cast_key = '1'
        self.actually_cast_time = self.cast_time_1
        self.inventory_x = None
        self.inventory_y = None
        self.bank_x = None
        self.bank_y = None

        self.mana_low_x_y = None
        self.mana_full_x_y = None

        self.mana_pixel_low = None
        self.mana_pixel_full = None

        self.skill_x_y = None
        self.skill_pixel = None

        self.value_for_count_without_result = 30
        self.count_without_result = self.value_for_count_without_result

    def cast_time_selector(self, cast_key):
        match cast_key:
            case '1':
                return self.cast_time_1
            case '2':
                return self.cast_time_2
            case '3':
                return self.cast_time_3
            case '4':
                return self.cast_time_4
            case '5':
                return self.cast_time_5
            case '6':
                return self.cast_time_6
            case '7':
                return self.cast_time_7
            case '8':
                return self.cast_time_8
            case '9':
                return self.cast_time_9
            case _:
                exit("Спелы закончились.")


    def set_inventory_and_bank_position(self):
        print(f"Ожидание нажатия {self.set_position_key} для инвентаря...")
        while True:
            if keyboard.is_pressed(self.set_position_key):
                self.inventory_x, self.inventory_y = pyautogui.position()
                self.wait(1)
                print(f"Going to break")
                break

        print(f"Ожидание нажатия {self.set_position_key} для банка...")
        while True:
            if keyboard.is_pressed(self.set_position_key):
                self.bank_x, self.bank_y = pyautogui.position()
                self.wait(1)
                print(f"Going to break")
                break

    def set_mana_position(self):
        print(f"Ожидание нажатия {self.set_position_key} для полоски маны при низком показателе...")
        while True:
            if keyboard.is_pressed(self.set_position_key):
                self.mana_low_x_y = pyautogui.position()
                self.mana_pixel_low = self.get_pixel(self.mana_low_x_y[0], self.mana_low_x_y[1])
                self.wait(1)
                print(f"Going to break")
                break

        print(f"Ожидание нажатия {self.set_position_key} для полоски маны при полном показателе...")
        while True:
            if keyboard.is_pressed(self.set_position_key):
                self.mana_full_x_y = pyautogui.position()
                self.mana_pixel_full = self.get_pixel(self.mana_full_x_y[0], self.mana_full_x_y[1])
                self.wait(1)
                print(f"Going to break")
                break

    def set_skill_position(self):
        print(f"Ожидание нажатия {self.set_position_key} для полоски скилла в самом начале...")
        while True:
            if keyboard.is_pressed(self.set_position_key):
                self.skill_x_y = pyautogui.position()
                self.skill_pixel = self.get_pixel(self.skill_x_y[0], self.skill_x_y[1])
                self.wait(1)
                print(f"Going to break")
                break

    def skill_go_up_checking(self):
        if not self.pixel_checking("skill"):
            if not self.cast_count_without_result():
                self.next_spell()
        else:
            self.count_without_result = self.value_for_count_without_result

    def cast_count_without_result(self):
        self.count_without_result -= 1
        if self.count_without_result > 0:
            return True
        else:
            self.count_without_result = self.value_for_count_without_result
            return False

    def next_spell(self):
        new_spell_number = int(self.cast_key) + 1
        if new_spell_number < 10:
            self.cast_key = str(new_spell_number)
            self.actually_cast_time = self.cast_time_selector(self.cast_key)
        else:
            exit("Спелы закончились.")

    def pixel_checking(self, full_or_low_or_skill):
        sensitivity = 3

        def check(index_rgb: int):
            if -sensitivity < (old_pixel[index_rgb] - new_pixel[index_rgb]) < sensitivity:
                return True
            else:
                return False

        match full_or_low_or_skill:
            case "low":
                new_pixel = self.get_pixel(self.mana_low_x_y[0], self.mana_low_x_y[1])
                old_pixel = self.mana_pixel_low
                if check(0) and check(1) and check(2):
                    return False
                else:
                    return True

            case "full":
                new_pixel = self.get_pixel(self.mana_full_x_y[0], self.mana_full_x_y[1])
                old_pixel = self.mana_pixel_full
                if check(0) and check(1) and check(2):
                    return True
                else:
                    return False

            case "skill":
                new_pixel = self.get_pixel(self.skill_x_y[0], self.skill_x_y[1])
                old_pixel = self.skill_pixel
                if check(0) and check(1) and check(2):
                    return True
                else:
                    return False

            case _:
                new_pixel = ('', '', '')
                old_pixel = (0, 0, 0)

    def right_mouse_press(self, x: int, y: int):
        pyautogui.click(x=x, y=y, button="right")

    def bank_press(self):

        self.right_mouse_press(x=self.bank_x, y=self.bank_y)
        self.wait(0.2)
        self.right_mouse_press(x=self.bank_x, y=self.bank_y)
        self.wait(0.2)
        self.right_mouse_press(x=self.bank_x, y=self.bank_y)

    def get_pixel(self, x, y):
        hdc = ctypes.windll.user32.GetDC(0)
        color = ctypes.windll.gdi32.GetPixel(hdc, x, y)
        r = color % 256
        g = (color // 256) % 256
        b = color // (256 ** 2)
        ctypes.windll.user32.ReleaseDC(0, hdc)
        return (r, g, b)

    def inventory_press(self):

        self.right_mouse_press(x=self.inventory_x, y=self.inventory_y)
        self.wait(0.2)
        self.right_mouse_press(x=self.inventory_x, y=self.inventory_y)
        self.wait(0.2)
        self.right_mouse_press(x=self.inventory_x, y=self.inventory_y)

    def nothing(self):
        return None

    def resting(self):
        self.press(self.rest_key)

        while not self.pixel_checking("full"):
            self.wait(1)

    def custom(self):  # Главный метод, весь код писать сюда

        self.set_inventory_and_bank_position()
        self.set_mana_position()
        self.set_skill_position()

        while not self.isStop and not self.exitKey:
            additional_waiting = 0.5
            while not self.pixel_checking("low"):
                self.skill_go_up_checking()
                self.hold("w") if self.moving_mode else self.nothing()
                self.press(self.cast_key)
                self.inventory_press()
                self.wait(self.actually_cast_time)

                self.release("w") if self.moving_mode else self.nothing()
                self.hold("s") if self.moving_mode else self.nothing()

                if self.cast_twice:
                    self.press(self.cast_key)
                self.wait(additional_waiting)

                self.release("s") if self.moving_mode else self.nothing()
                self.bank_press()
                self.wait(0.01)

            self.resting()


def run():
    script_class = Script()  # инициализация класса (сменить название на актуальное)
    script_class.custom()


if __name__ == "__main__":
    run()
