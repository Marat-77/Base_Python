# /Zakiev_Marat_dz_7/zakiev_marat_lesson_7_2
# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание:
# структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
# conf.yaml

import yaml
import os


# ############################################################## _read_conf
def recursive_func3(value, m2_list_project, path_str='', count=0):
    for key, value in value.items():
        if count == 0:
            path_str = '/' + key + '/'
        else:
            path_str += key + '/'
        for k_ey, value in value.items():
            if k_ey == 'files':
                m2_list_project += [path_str] + [value]
            elif k_ey == 'dirs':
                count += 1
                recursive_func3(value, m2_list_project, path_str, count)
            else:
                path_str = ''


def read_conf():
    input_file = 'conf.yaml'
    with open(input_file) as fh:
        read_data = yaml.load(fh, Loader=yaml.FullLoader)
    #
    root = str()
    path_root = list()
    m2_list_project = []
    for key, value in read_data.items():
        root = key
        for ke_y, valu_e in value.items():
            if ke_y == 'files':
                path_root = [root, valu_e]  # path_root=['my_project', ['readme.txt']]
            elif ke_y == 'dirs':
                recursive_func3(valu_e, m2_list_project)
    # функция выдаёт кортеж (root, path_root, m2_list_project),
    # где root - строка "название_проекта",
    # path_root - список ["название_проекта", ['readme.txt']],
    # m2_list_project - список структуры проекта
    return root, path_root, m2_list_project
# ############################################################## _read_conf


# создание корневой папки проекта:
def make_new_dir(new_dir):
    n = 1
    if os.path.isdir(new_dir):
        print(f'1. {new_dir} уже есть')
        double_new_dir = f'{new_dir}_{str(n)}'
        while os.path.isdir(double_new_dir):
            print(f'2. {double_new_dir} уже есть')
            n += 1
            double_new_dir = f'{new_dir}_{str(n)}'
        new_dir = double_new_dir
        os.mkdir(new_dir)
        print(f'создана папка проекта "{new_dir}"')
    else:
        os.mkdir(new_dir)
        print(f'создана папка проекта "{new_dir}"')
    return new_dir


# ##########################################################################################
# function create_files
def create_files(input_path):
    f = open(input_path, 'w', encoding='utf-8')
    f.close()
    if os.path.isfile(input_path):
        print(f'{input_path} создан')  # - проверили существование файла
# ##########################################################################################


# ########################################################### make_subdirs
# создание подпапок и файлов:
def make_subdirs(root_dir, readme_path, list_struct):
    # #################################### создание readme.txt в коневой папке проекта
    text = f'Проект {root_dir}'  # текст для файла readme.txt
    for rf in readme_path[1]:
        if rf == 'readme.txt':
            # если есть readme.txt
            rf = f'{readme_path[0]}/{rf}'
            with open(rf, 'w', encoding='utf-8') as f_readme:
                f_readme.write(text)  # пишем текст в файл readme.txt
            if os.path.isfile(rf):
                print(f'{rf} создан')  # - проверили существование файла
        else:
            # если кроме readme.txt должны быть другие файлы
            rf = f'{readme_path[0]}/{rf}'
            create_files(rf)
    # #################################### создание readme.txt в коневой папке проекта
    path = ''
    for i in list_struct:
        if type(i) == str:
            i = i.replace('/mainapp/authapp/', '/authapp/')  # hack
            path = root_dir + i
            try:
                os.makedirs(path)  # создает подпапки
            except FileExistsError:
                print('Папка уже существует')
        elif type(i) == list:
            for j in i:
                path_f = path + j
                create_files(path_f)  # создает файлы
# ########################################################### make_subdirs


def create_project(project_name, readme_path, list_struct):
    project_root = make_new_dir(project_name)
    readme_path = [project_root, readme_path[1]]
    make_subdirs(project_root, readme_path, list_struct)
    print('Отчет:')
    for root, dirs, files in os.walk(project_root):
        print(f'каталог {root} создан')  # проверка созданных каталогов
        if files:
            print(f'файлы {files} созданы')  # проверка созданных файлов


if __name__ == '__main__':
    # read_conf()  # читаем my_conf.yaml
    # create_project()  # создаем папки и файлы проекта
    project_name_, path_readme_, list_structure = read_conf()
    create_project(project_name_, path_readme_, list_structure)  #
#
