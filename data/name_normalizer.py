

name_normalize_data = {

    'attacker': "Тренька парри",
    'destroyerPickaxe': "Разрушение домов",
    'easyFlux': 'Облегчение флюксинга',
    'foliageHider': 'Перезагрузка листвы',
    'intBoost': 'Прокачка инты',
    'mentalTraining': 'Прокачка ментала',
    'spam': 'Собственный скрипт',
    'domination': 'Тэйминг\\Доминация',

}


def do(name):
    if name in name_normalize_data:
        return name_normalize_data[name]
    else:
        return None