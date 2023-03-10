import os

from scripts.base import BaseScript  # обязательный импорт для наследования
import tools.jsonOper


class Script(BaseScript):  # Название класса (должен отличаться от других названий скриптов)

    name = file_name = os.path.basename(__file__)[:-3]
    config = {
        "activate_key": "",
        "key1": {"name": "", "value": ""},
        "key2": {"name": "", "value": ""},
        "key3": {"name": "", "value": ""},
        "key4": {"name": "", "value": ""},
        "key5": {"name": "", "value": ""},
        "key6": {"name": "", "value": ""},
    }
    description = ""
    keys = tools.jsonOper.loadKeys(name) if name != "NewScriptSample" else config
    ready = True if keys["activate_key"] != "" else False



    def __init__(self):
        super().__init__()  # инициализация класса после наследования

        """                   Ключи - Обязательное                   """

        self.name = Script.name  # имя в базе ключей
        self.keys = Script.keys  # загрузка настройки всех ключей данного скрипта
        self.keyActivate = self.keys["activate_key"]  # кнопка активации скрипта
        # обязательно скопировать ключ-значение "base", и переименовать согласно значению в self.name

        """ Полезное, но имеющее значение по дефолту, удалить при ненадобности """
        self.ready = True if self.keys["activate_key"] != "" else False  # Включает\Выключает скрипт в мейновом запуске
        self.game = "Mortal Online 2  "
        self.loop = True  # True активирует бесконечный цикл метода custom()
        self.debug = True  # Логи на стандартные функции
        self.window_w = 1920  # Ширина экрана (лучше настраивать через ключи)
        self.window_h = 1080  # Высота экрана (лучше настраивать через ключи)

        """ Кастомные атрибуты писать здесь """

    def custom(self):  # Главный метод, весь код писать сюда
        pass


def run():
    script_class = Script()  # инициализация класса (сменить название на актуальное)
    script_class.custom()


if __name__ == "__main__":
    run()
