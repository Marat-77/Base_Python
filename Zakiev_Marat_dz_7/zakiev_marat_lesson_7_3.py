# /Zakiev_Marat_dz_7/zakiev_marat_lesson_7_3
#
# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates,
# например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание:
# исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.
#

import os
import shutil


def myproject_walk():
    z = os.listdir()
    for i_file in z:
        if os.path.isdir(i_file) and i_file.find('project'):
            for root, dirs, files in os.walk(i_file):
                if dirs == ['templates']:
                    t_root = root.replace('\\', '/') + '/templates'
                    dst = f'{i_file}/templates/'
                    shutil.copytree(t_root, dst, dirs_exist_ok=True)
                    print(f'каталог {t_root} с подпапками и файлами скопирован в {dst}')


if __name__ == '__main__':
    myproject_walk()
    print('Копирование завершено.')

#
