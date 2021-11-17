# /Zakiev_Marat_dz_7/zakiev_marat_lesson_7_5
#
# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]),
# например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
#
# some_data и some_data/other_data - по 1000 файлов в каждом. Суммарно = 2000.
import json
import os
from pathlib import Path


def mnew_find(my_path, n):
    if n == 100:
        x = 0
    else:
        x = n / 10
    count = 0
    big_count = 0
    files_list = []
    for root, dirs, files in os.walk(my_path):
        for i in files:
            i_file = root.replace('\\', '/') + '/' + i
            i_file_size = Path(i_file).stat().st_size
            if x <= i_file_size < n:
                files_list.append(i)
                count += 1
            if i_file_size >= n:
                big_count += 1
    tuple_count = (count, files_list)
    new_dict = {n: tuple_count}
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
    with open('some_data_summary.json', 'w') as write_json:
        json.dump(n_dict, write_json)


if __name__ == '__main__':
    find_pathlib()
#
# well done!
