# Zakiev_Marat_dz_5/zakiev_marat_lesson_5_4.py
# draft_zakiev_marat_lesson_5_4.py

# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.


from sys import getsizeof
from time import perf_counter


def gen_bigger_than_last(num_src):
    start = perf_counter()
    temp_i = 0
    for i in num_src:
        if i > temp_i:
            yield i
        temp_i = i
        #
    print(f'{perf_counter() - start} - perf_counter gen_bigger_than_last')


def for_bigger_than_last(nums):
    start = perf_counter()
    temp_i = 0
    new_list = []
    for i in nums:
        if i > temp_i:
            new_list.append(i)
        temp_i = i
    print(f'{perf_counter() - start} - perf_counter for i in nums -> new_list')
    print(f'{getsizeof(new_list)} - getsizeof new_list')
    print(new_list)


if __name__ == '__main__':
    src = [622, 70, 89, 50, 384, 69, 305, 54, 531, 46, 283, 3, 822, 76, 330, 68, 215, 13, 301, 2]
    for_bigger_than_last(src)
    print('**' * 20)
    gen_numbers = gen_bigger_than_last(src)
    print(f'{getsizeof(gen_numbers)} - getsizeof gen_numbers')
    gen_list = []
    for g in gen_numbers:
        gen_list.append(g)
    print(f'{getsizeof(gen_list)} - getsizeof gen_list')
    print(gen_list)
