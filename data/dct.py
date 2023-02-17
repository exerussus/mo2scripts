
from data.descriptions import *


dct = {
    "base": [{
                        "activate_key": "",
                        "key1": {"name": "", "value": ""},
                        "key2": {"name": "", "value": ""},
                        "key3": {"name": "", "value": ""},
                        "key4": {"name": "", "value": ""},
                        "key5": {"name": "", "value": ""},
                        "key6": {"name": "", "value": ""},
                    },
                    "Описание"
                    ],

    "domination": [{
                        "activate_key": "f2",
                        "key1": {"name": "action_key", "value": "v"},
                        "key2": {"name": "holding_time", "value": "5"},
                        "key3": {"name": "domination", "value": "1"}
                    },
                    domination_description
                    ],



       "spam": [{
                        "activate_key": "f5",
                        "key1": {"name": "1. Кнопка нажатия", "value": ""},
                        "key2": {"name": "1. Пауза после нажатия", "value": ""},

                        "key3": {"name": "2. Кнопка зажатия", "value": ""},
                        "key4": {"name": "2. Время зажатия", "value": ""},

                        "key5": {"name": "1-2. Количество повторений", "value": ""},

                        "key6": {"name": "3. Кнопка нажатия", "value": ""},
                        "key7": {"name": "3. Пауза после нажатия", "value": ""},

                        "key8": {"name": "4. Кнопка зажатия", "value": ""},
                        "key9": {"name": "4. Время зажатия", "value": ""},

                        "key10": {"name": "3-4. Количество повторений", "value": ""},
                    },
                    spam_description
                    ],

       "attacker": [{
                        "activate_key": "f3",
                        "key1": {"name": "Удар сверху", "value": "q"},
                        "key2": {"name": "Удар справа", "value": "g"},
                        "key3": {"name": "Удар слева", "value": "h"},
                        "key4": {"name": "Удар снизу", "value": "f"},
                        "key5": {"name": "Мод", "value": "1"},
                        "key6": {"name": "Ожидание между ударами", "value": "0.6"},
                        "key7": {"name": "Время зарядки удара", "value": "0.1"},
                        "key8": {"name": "Финт", "value": "e"},
                        "key9": {"name": "Включить финты", "value": "0"},
                        "key10": {"name": "Включить повороты", "value": "0"},

                    },
                    attacker_description
                    ],

       "easyFlux": [{
                        "activate_key": "",
                        "key1": {"name": "Изгнание", "value": ""},
                        "key2": {"name": "Вызов спирита", "value": ""},
                        "key3": {"name": "Кнопка атаки", "value": ""},
                        "key4": {"name": "Каст на себя", "value": ""}
                    },
                    "Описание"
                    ],

       "mentalTraining": [{
                        "activate_key": "",
                        "key1": {"name": "Клавиша водички", "value": "1"},
                        "key2": {"name": "Количество повторений водички", "value": "15"},
                        "key3": {"name": "Клавиша хила", "value": "2"},
                        "key4": {"name": "Количество повторений хила", "value": "1"},
                        "key5": {"name": "Клавиша отдыха", "value": "0"},
                        "key6": {"name": "Время отдыха", "value": "50"},
                        "key7": {"name": "Каст на себя", "value": "k"}
                    },
                    "Если хил не нужен - оставьте поле пустым."
                    ],

       "destroyerPickaxe": [{
                        "activate_key": "f6",
                        "key1": {"name": "Атака сверху", "value": "q"},  # атака сверху
                        "key2": {"name": "Вытащить оружие", "value": "x"},  # вытащить оружие
                        "key3": {"name": "Прыжок", "value": "space"},  # прыжок
                        "key4": {"name": "Вперёд", "value": "w"},  # вперёд
                        "key5": {"name": "Назад", "value": "s"},  # назад
                        "key6": {"name": "Зарядка удара", "value": "0.295"},  # зарядка удара
                        "key7": {"name": "Отмашка", "value": "0.55"},  # отмашка
                        "key8": {"name": "Время ходьбы назад", "value": "3"},  # время ходьбы назад
                        "key9": {"name": "Время ходьбы вперёд", "value": "3.1"},  # время ходьбы вперёд

                        "key10": {"name": "Прочность", "value": "250"},  # Прочность
                        "key11": {"name": "Трата прочки за удар", "value": "0.14"},  # Трата прочности за удар

                        "key12": {"name": "1 доп. ячейка", "value": "t"},  #
                        "key13": {"name": "2 доп. ячейка", "value": "g"},  #
                        "key14": {"name": "3 доп. ячейка", "value": "b"},  #
                        "key15": {"name": "4 доп. ячейка", "value": "y"},  #
                        "key16": {"name": "5 доп. ячейка", "value": "h"},  #
                        "key17": {"name": "6 доп. ячейка", "value": "n"},  #
                        "key18": {"name": "7 доп. ячейка", "value": "u"},  #
                        "key19": {"name": "8 доп. ячейка", "value": "j"},  #
                        "key20": {"name": "9 доп. ячейка", "value": "m"},  #
                    },
                    "Описание"
                    ],

       "intBoost": [{
                        "activate_key": "",
                        "key2": {"name": "Ширина окна", "value": "1920"},
                        "key3": {"name": "Высота окна", "value": "1080"},
                    },
                    intBoost_description
                    ],

       "foliageHider": [{
                        "activate_key": "f4",
                        "key1": {"name": "Кнопка перезагрузки листвы (любая кроме f7 и f9)", "value": "f4"},
                        "key2": {"name": "Ширина окна", "value": "1920"},
                        "key3": {"name": "Высота окна", "value": "1080"},
                    },
                    "Описание"
                    ],

       "autoCraft": [{
                        "activate_key": "",
                        "key1": {"name": "Ширина окна", "value": "1920"},
                        "key2": {"name": "Высота окна", "value": "1080"},
                    },
                    "Описание"
                    ],

       }