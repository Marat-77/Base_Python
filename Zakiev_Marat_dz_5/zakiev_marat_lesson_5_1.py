# Zakiev_Marat_dz_5/zakiev_marat_lesson_5_1.py

# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...


def odd_nums(n):
    for i in range(1, n, 2):
        yield i


def main():
    # print(type(odd_nums(15)))  # <class 'generator'>
    # print(type(odd_nums))  # <class 'function'>
    # -------------------------------------
    gen = odd_nums(15)
    print(next(gen))  # 1
    print(next(gen))  # 3
    print(next(gen))  # 5
    print(next(gen))  # 7
    print(next(gen))  # 9
    print(next(gen))  # 11
    print(next(gen))  # 13
    # print(next(gen))  # StopIteration
    # print(next(gen))  # не выполнится
    # -------------------------------------


if __name__ == '__main__':
    main()

# well done!
