from scripts.base import BaseScript  # обязательный импорт для наследования
import autoit
import time


class Script(BaseScript):  # Название класса (должен отличаться от других названий скриптов)

    def __init__(self):
        super().__init__()  # инициализация класса после наследования

        """                   Ключи - Обязательное                   """

        self.name = "autoCraft"  # имя в базе ключей
        self.keys = self.keys_data[self.name][0]  # загрузка настройки всех ключей данного скрипта
        self.keyActivate = self.keys["activate_key"]  # кнопка активации скрипта
        self.ready = True if self.keys["activate_key"] != "" else False
        # обязательно скопировать ключ-значение "base", и переименовать согласно значению в self.name
        """ Полезное, но имеющее значение по дефолту, удалить при ненадобности """
        self.ready = True if self.keys["activate_key"] != "" else False  # Включает\Выключает скрипт в мейновом запуске
        self.game = "Mortal Online 2  "
        self.loop = True  # True активирует бесконечный цикл метода custom()
        self.debug = True  # Логи на стандартные функции

        """ Кастомные атрибуты писать здесь """
        self.window_w = int(float(self.keys["key1"]["value"]))
        self.window_h = int(float(self.keys["key2"]["value"]))


    def custom(self):  # Главный метод, весь код писать сюда

        speed = 1
        time.sleep(2)
        while not self.isStop and not self.exitKey:
            autoit.mouse_move(speed=speed, x=self.clc_x(1835), y=self.clc_y(550))
            autoit.mouse_down("left")
            self.wait(30)
            autoit.mouse_up("left")
            self.wait(1)

            self.hold('lalt')
            self.wait(0.1)
            self.hold('lalt')

            self.mouse_click("right", 1620, 940)
            self.wait(0.1)
            self.mouse_click("right", 1620, 990)
            self.wait(0.1)
            self.mouse_click("right", 1620, 1040)
            self.wait(0.1)

            self.mouse_click("right", 1670, 940)
            self.wait(0.1)
            self.mouse_click("right", 1670, 990)
            self.wait(0.1)
            self.mouse_click("right", 1670, 1040)
            self.wait(0.1)

            self.mouse_click("right", 1720, 940)
            self.wait(0.1)
            self.mouse_click("right", 1720, 990)
            self.wait(0.1)
            self.mouse_click("right", 1720, 1040)
            self.wait(0.1)

            self.mouse_click("right", 1780, 940)
            self.wait(0.1)
            self.mouse_click("right", 1780, 990)
            self.wait(0.1)
            self.mouse_click("right", 1780, 1040)
            self.wait(0.1)

            self.mouse_click("right", 1820, 940)
            self.wait(0.1)
            self.mouse_click("right", 1820, 990)
            self.wait(0.1)
            self.mouse_click("right", 1820, 1040)
            self.wait(0.1)

            self.mouse_click("right", 1880, 940)
            self.wait(0.1)
            self.mouse_click("right", 1880, 990)
            self.wait(0.1)
            self.mouse_click("right", 1880, 1040)
            self.wait(0.1)

            self.release('lalt')
            self.wait(0.1)
            self.release('lalt')
            self.wait(1)
            self.release('lalt')
            self.wait(1)

            self.mouse_click("left", 890, 970)
            self.wait(0.5)
            self.mouse_click("left", 890, 970)
            self.wait(1)

            # self.press('1')
            # self.wait(0.05)
            #
            # autoit.mouse_click("left", speed=speed, x=self.clc_x(1720), y=self.clc_y(1050))
            #
            # self.wait(0.05)
            # autoit.mouse_click("right", speed=speed, x=self.clc_x(1750), y=self.clc_y(1030))
            # autoit.mouse_move(speed=speed, x=self.clc_x(960), y=self.clc_y(630))
            # self.wait(0.05)
            #
            # autoit.mouse_down("left")
            # self.wait(1.45)
            # autoit.mouse_up("left")
            # self.wait(0.1)
            # self.release('lshift')


def run():
    script_class = Script()  # инициализация класса (сменить название на актуальное)
    script_class.custom()


if __name__ == "__main__":
    run()
