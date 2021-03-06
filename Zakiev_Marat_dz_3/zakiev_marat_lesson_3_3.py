# zakiev_marat_lesson_3_3
#
# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имён,
# а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
#
#
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?


def thesaurus(names: list) -> dict:
    """
    Function get list of names and save into dict
    функция принимает список имен и вносит в словарь
    :param names: list - incoming list of names
    :return: dict
    """
    # функция принимает список имен и вносит в словарь в виде '(инициал)': [список имен]
    for val_name in names:
        if not val_name.isspace():
            # - исключаем непечатные символы, избежим ошибки в случае если был введен только пробел/ы.
            # имя из полученного списка с удаленными пробелами (слева и справа) и с заглавной:
            val_name = val_name.strip().title()
            name_key = val_name[0]  # из первого элемента строки (имени) создаем ключ
            if dict_names.get(name_key) is None:
                # если ключа в словаре нет:
                dict_names[name_key] = [val_name]  # создаем ключ и значение
            else:
                # иначе (такой ключ есть):
                if (dict_names.get(name_key)).count(val_name) == 0:
                    # если в списке такое имя встречается 0 раз (чтобы избежать дублирования имен)!
                    val_names = dict_names.get(name_key) + [val_name]  # добавим имя в список этого ключа
                    dict_names[name_key] = val_names  # запишем полученный список в этот ключ
    return dict_names  # выдаём полученный словарь


x_input_name = ''
dict_names = dict()
while x_input_name != '000':
    x_input_name = input(
        'Введите имя (например: Иван) или несколько имен через запятую (например: Яна, Max)\n'
        '[для выхода из программы введите "000"] : '
    )
    if x_input_name == '000':
        print('Вы вышли из программы')
    else:
        x_input_name = x_input_name.strip(',')  # удаляет запятую слева и справа строки
        input_names = x_input_name.split(',')  # разбиваем полученную строку по ',' и получаем список names
        thesaurus(input_names)  # передаем список в функцию
        print('*' * 45)
        for keys, values in dict_names.items():
            print(f'{keys}: {values}')  # выводим полученный словарь построчно


# для теста:
# print('test:')
# x_input_name = 'Иван, Илья,   , Анна ,  петр,  R2-D2, Max, Guido, Антон, Анна, Иван, Иван, Жан Поль, Rafael'
# input_names = x_input_name.split(',')  # разбиваем полученную строку по ',' и получаем список names
# thesaurus(input_names)  # передаем список в функцию
# print('*' * 45)
# print(dict_names)  # выводим полученный словарь
