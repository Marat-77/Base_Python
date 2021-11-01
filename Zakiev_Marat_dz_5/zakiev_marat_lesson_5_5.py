# zakiev_marat_lesson_5_5.py

# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.


# import
from sys import getsizeof
from time import perf_counter


def main():
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 8, 38, 74, 92, 65, 12, 123, 456, 789, 147, 258, 399, 369,]
    print(src)  # исходный список
    print(f'{getsizeof(src)} - getsizeof src')

    # for_unique_list
    start = perf_counter()
    unique_list = []
    for i in src:
        if src.count(i) == 1:
            unique_list.append(i)
    time_for_unique_list = perf_counter() - start
    print(unique_list)  # список уникальных элементов из исходного списка
    # -------------------------------------------------------------------------- optimization ***
    print('optimization')
    # generator
    start = perf_counter()
    gen = (i for i in src if src.count(i) == 1)
    result = [*gen]
    time_generator_result = perf_counter() - start
    # можно еще так записать:
    # result = [*(i for i in src if src.count(i) == 1)]
    print(result)  # список уникальных элементов с помощью генератора

    print('*' * 50)
    print('Сравнение размеров:')
    print(f'{getsizeof(unique_list)} - getsizeof unique_list')
    print(f'{getsizeof(gen)} - getsizeof gen')
    print(f'{getsizeof(result)} - getsizeof result')
    print('Сравнение скорости:')
    print(f'time_for_unique_list = {time_for_unique_list}')
    print(f'time_generator_result = {time_generator_result}')


if __name__ == '__main__':
    main()

# ! В чем оптимизация:
# размер полученных списков одинаковый и скорость выполнения примерно одинаковая,
# но если не выводить генератор в result (result = [*gen]), то генераторное выражение занимает меньше памяти,
# а на больших списках гораздо меньше памяти!!!
