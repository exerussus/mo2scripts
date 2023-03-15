from scripts.base import BaseScript  # обязательный импорт для наследования
import pyautogui
import keyboard
import autoit
import os
from tools import jsonOper

class Script(BaseScript):  # Название класса (должен отличаться от других названий скриптов)

    name = file_name = os.path.basename(__file__)[:-3]
    config = {
        "activate_key": "f4",
        "key1": {"name": "Кнопка перезагрузки листвы (любая кроме f7 и f9)", "value": "f4"},
        "key2": {"name": "Ширина окна", "value": "1920"},
        "key3": {"name": "Высота окна", "value": "1080"},
    }
    description = ""
    russian = 'Отключение листвы'
    keys = jsonOper.loadKeys(name)
    ready = True if keys["activate_key"] != "" else False
    def __init__(self):
        super().__init__()  # инициализация класса после наследования

        """                   Ключи - Обязательное                   """

        self.name = Script.name  # имя в базе ключей
        self.keys = Script.keys # загрузка настройки всех ключей данного скрипта
        self.keyActivate = self.keys["activate_key"]  # кнопка активации скрипта
        self.reload_foliage_key = self.keys["key1"]["value"]
        self.window_w = int(self.keys["key2"]["value"])
        self.window_h = int(self.keys["key3"]["value"])
        self.holding_left = False
        self.timer = 0
        self.toggle = False
        self.first = False

        pyautogui.FAILSAFE = False

        """ Кастомные атрибуты писать здесь """

    def clc_x(self, mod):
        return round(self.window_w * mod)

    def clc_y(self, mod):
        return round(self.window_h * mod)

    def custom(self):  # Главный метод, весь код писать сюда
        speed = 1
        if keyboard.is_pressed('f4') and not self.first:
            pyautogui.press('escape')
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.5), y=self.clc_y(0.388))  # x=961, y=420
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.38), y=self.clc_y(0.682))  # x=730, y=737
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.336), y=self.clc_y(0.737))  # x=647, y=797
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.375), y=self.clc_y(0.564))  # x=720, y=610
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.354), y=self.clc_y(0.676))  # x=680, y=730
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.427), y=self.clc_y(0.907))  # x=820, y=980
            self.toggle = True
            self.first = True
            self.wait(0.3)

        elif keyboard.is_pressed('f4') and not self.toggle:
            pyautogui.press('escape')
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.5), y=self.clc_y(0.388))
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.375), y=self.clc_y(0.564))
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.354), y=self.clc_y(0.676))
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.427), y=self.clc_y(0.907))  # x=820, y=980
            self.toggle = True
            self.wait(0.3)
        elif keyboard.is_pressed('f4') and self.toggle:
            pyautogui.press('escape')
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.5), y=self.clc_y(0.388))  # x=961, y=420
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.375), y=self.clc_y(0.564))  # x=720, y=610
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.354), y=self.clc_y(0.593))  #
            autoit.mouse_click("left", speed=speed, x=self.clc_x(0.427), y=self.clc_y(0.907))  # x=820, y=980
            self.toggle = False
            self.wait(0.3)


def run():
    script_class = Script()  # инициализация класса (сменить название на актуальное)
    script_class.custom()


if __name__ == "__main__":
    run()
