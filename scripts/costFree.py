import os

import keyboard
import pyautogui

from scripts.base import BaseScript  # обязательный импорт для наследования
import tools.jsonOper


class Script(BaseScript):  # Название класса (должен отличаться от других названий скриптов)

    name = file_name = os.path.basename(__file__)[:-3]
    config = {
        "activate_key": "",
        "key1": {"name": "Клавиша активации", "value": "q"},
        "key2": {"name": "Клавиша каста", "value": "1"},
        "key3": {"name": "Количество кастов", "value": "10"},
        "key4": {"name": "Клавиша отдыха", "value": "0"},
        "key5": {"name": "Время отдыха", "value": "40"},
        "key6": {"name": "Время каста", "value": "4"},
        "key7": {"name": "Повторное нажатие для каста", "value": "1"},
    }
    description = "После запуска скрипта, надо навести мышь\n" \
                  "на ячейку инвентаря и нажать клавишу активации.\n" \
                  "После этого наведите на ячейку в банке и нажмите\n" \
                  "клавишу активации. После этого, когда будете готовы,\n" \
                  "нажмите ещё раз клавишу активации.\n"
    keys = tools.jsonOper.loadKeys(name)
    ready = True if keys["activate_key"] != "" else False


    def __init__(self):
        super().__init__()  # инициализация класса после наследования

        """                   Ключи - Обязательное                   """

        self.name = Script.name  # имя в базе ключей
        self.keys = Script.keys # загрузка настройки всех ключей данного скрипта
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
        self.cast_key = self.keys["key2"]["value"]
        self.cast_count = int(self.keys["key3"]["value"])
        self.rest_key = self.keys["key4"]["value"]
        self.rest_seconds = float(self.keys["key5"]["value"])
        self.cast_time = float(self.keys["key6"]["value"])
        self.cast_twice = True if self.keys["key7"]["value"] == "1" else False
        self.inventory_x = None
        self.inventory_y = None
        self.bank_x = None
        self.bank_y = None

    def right_mouse_press(self, x: int, y: int):
        pyautogui.click(x=x, y=y, button="right")

    def bank_press(self):

        self.right_mouse_press(x=self.bank_x, y=self.bank_y)
        self.wait(0.2)
        self.right_mouse_press(x=self.bank_x, y=self.bank_y)
        self.wait(0.2)
        self.right_mouse_press(x=self.bank_x, y=self.bank_y)

    def inventory_press(self):

        self.right_mouse_press(x=self.inventory_x, y=self.inventory_y)
        self.wait(0.2)
        self.right_mouse_press(x=self.inventory_x, y=self.inventory_y)
        self.wait(0.2)
        self.right_mouse_press(x=self.inventory_x, y=self.inventory_y)

    def custom(self):  # Главный метод, весь код писать сюда
        print(f"Ожидание нажатия {self.set_position_key} для инвентаря...")
        while True:
            if keyboard.is_pressed(self.set_position_key):
                self.inventory_x, self.inventory_y = pyautogui.position()
                self.wait(2)
                print(f"Going to break")
                break

        print(f"Ожидание нажатия {self.set_position_key} для банка...")
        while True:
            if keyboard.is_pressed(self.set_position_key):
                self.bank_x, self.bank_y = pyautogui.position()
                self.wait(2)
                print(f"Going to break")
                break

        while not self.isStop and not self.exitKey:
            additional_waiting = 0.4
            for _ in range(self.cast_count):
                self.hold("w")
                self.press(self.cast_key)
                self.inventory_press()
                self.wait(self.cast_time)
                self.release("w")
                self.hold("s")

                if self.cast_twice:
                    self.press(self.cast_key)
                    self.wait(0.3)
                self.wait(additional_waiting)
                self.release("s")
                self.bank_press()
                self.wait(0.01)

            self.press(self.rest_key)
            self.wait(self.rest_seconds)


def run():
    script_class = Script()  # инициализация класса (сменить название на актуальное)
    script_class.custom()


if __name__ == "__main__":
    run()
