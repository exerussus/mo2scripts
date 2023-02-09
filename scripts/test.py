from scripts.base import BaseScript  # обязательный импорт для наследования


class Script(BaseScript):  # Название класса (должен отличаться от других названий скриптов)

    def __init__(self):
        super().__init__()  # инициализация класса после наследования

        """                   Ключи - Обязательное                   """

        self.name = "base"  # имя в базе ключей
        self.keys = self.keys_data[self.name][0]  # загрузка настройки всех ключей данного скрипта
        self.keyActivate = self.keys["activate_key"]  # кнопка активации скрипта
        # обязательно скопировать ключ-значение "base", и переименовать согласно значению в self.name
        """ Полезное, но имеющее значение по дефолту, удалить при ненадобности """
        self.game = "Mortal Online 2  "
        self.loop = True  # True активирует бесконечный цикл метода custom()
        self.debug = True  # Логи на стандартные функции
        self.ready = False

        """ Кастомные атрибуты писать здесь """

    def water_pain(self, count):
        for _ in range(count):
            self.hold_and_release_wait('w', 0.3)
            self.wait(0.2)
            self.hold_and_release_wait('space', 0.2)
            self.wait(0.3)
            self.hold_and_release_wait('s', 0.3)
            self.wait(0.2)

            self.press("c")
            self.wait(1.7)
            self.press('f')
            self.wait(0.5)

    def healing(self, count):
        for _ in range(count):
            self.press("4")
            self.wait(2)
            self.press('f')
            self.wait(0.5)

    def resting(self, sec):
        self.press('0')
        self.wait(sec)

    def custom(self):  # Главный метод, весь код писать сюда
        self.hold('left')
        self.wait(2)
        # self.water_pain(35)
        # self.healing(2)
        # self.water_pain(15)
        # self.resting(30)
        # self.healing(2)




def run():
    script_class = Script()  # инициализация класса (сменить название на актуальное)
    script_class.run()


if __name__ == "__main__":
    run()
