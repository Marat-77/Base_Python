# /Zakiev_Marat_dz_7/zakiev_marat_lesson_7_4
#
# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
# например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
#
# some_data и some_data/other_data - по 1000 файлов в каждом. Суммарно = 2000.
import os
from pathlib import Path


def find_file(searching_path, n):
    if n == 100:
        x = 0
    else:
        x = n / 10
    with os.scandir(searching_path) as f_list:
        size_dict = {}
        count = 0
        for entry in f_list:
            input_path = f'{searching_path}/{entry.name}'
            # Unresolved attribute reference 'name' for class '_ScandirIterator'
            if entry.is_file():
                # Unresolved attribute reference 'is_file' for class '_ScandirIterator'
                if x <= os.stat(input_path).st_size < n:
                    count += 1
    size_dict[n] = count
    return size_dict


def find_size_files():
    searching_path = 'some_data'
    n = 100
    size_dict = find_file(searching_path, n)
    n *= 10
    size_dict.update(find_file(searching_path, n))
    n *= 10
    size_dict.update(find_file(searching_path, n))
    n *= 10
    size_dict.update(find_file(searching_path, n))
    n *= 10
    size_dict.update(find_file(searching_path, n))
    print(size_dict)
#


def mnew_find(my_path, n):
    if n == 100:
        x = 0
    else:
        x = n / 10
    count = 0
    big_count = 0
    for root, dirs, files in os.walk(my_path):
        for i in files:
            i_file = root.replace('\\', '/') + '/' + i
            i_file_size = Path(i_file).stat().st_size
            if x <= i_file_size < n:
                count += 1
            if i_file_size >= n:
                big_count += 1
    new_dict = {n: count}
    return new_dict, big_count


def find_pathlib():
    my_path = 'some_data'
    n = 100
    n_dict = {}
    big_flag = 1
    while big_flag != 0:
        n_dict.update(mnew_find(my_path, n)[0])
        big_flag = mnew_find(my_path, n)[1]
        n *= 10
    print(n_dict)
    # Вывод сообщения "Тут 15 файлов размером не более 100 байт...":
    print('Тут', end=' ')
    for k, v in n_dict.items():
        if k == 100:
            print(f'{v} файлов размером не более 100 байт', end='; ')
        elif k == 100 * 10:
            print(f'{v} файлов больше 100 и не больше {k} байт', end='; ')
        elif k == 100 * 10 * 10:
            print(f'{v} файлов больше 1000 и не больше {k} байт', end='; ')
        elif k == 100 * 10 * 10 * 10:
            print(f'{v} файлов больше 10000 и не больше {k} байт.')


if __name__ == '__main__':
    find_pathlib()
    # "find_pathlib()" - решение с помощью os.walk и pathlib Path().stat().st_size
    # не сразу придумал как сделать цикл, но что-то в итоге придумал
    # {100: 2, 1000: 20, 10000: 174, 100000: 1804}

    # find_size_files()
    # "find_size_files()"+"find_file()" - пробовал с помощью os.scandir и os.stat,
    # но для поиска в подпапках надо еще поковырять,
    # и еще Pycharm выдает "Problems":
    # entry.name - Unresolved attribute reference 'name' for class '_ScandirIterator'
    # entry.is_file - Unresolved attribute reference 'is_file' for class '_ScandirIterator'
    # - так и не понял что с этим предупреждением делать, но код работает:
    # {100: 1, 1000: 10, 10000: 87, 100000: 902, 1000000: 0}
#
# well done!
