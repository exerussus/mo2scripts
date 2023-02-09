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
        self.ready = True  # Включает\Выключает скрипт в мейновом запуске
        self.game = "Mortal Online 2  "
        self.loop = True  # True активирует бесконечный цикл метода custom()
        self.debug = True  # Логи на стандартные функции

        """ Кастомные атрибуты писать здесь """

    def custom(self):  # Главный метод, весь код писать сюда
        pass


def run():
    script_class = Script()  # инициализация класса (сменить название на актуальное)
    script_class.custom()


if __name__ == "__main__":
    run()
