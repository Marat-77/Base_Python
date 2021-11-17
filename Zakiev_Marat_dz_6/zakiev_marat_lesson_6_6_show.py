# # zakiev_marat_lesson_6_6_show

# 6. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1
#


# ########################################
# Нумерация записей начинается с 1. Примеры запуска скриптов:
# zakiev_marat_lesson_6_6_show 4
# zakiev_marat_lesson_6_6_show 3 7
# ########################################


def main():
    import sys
    param = sys.argv[1:]
    for arg in param:
        arg_int = int(arg)
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            count_line = 0
            for line in f:
                line = line.strip()
                count_line += 1
                if arg_int == count_line:
                    print(line)


if __name__ == '__main__':
    main()
#