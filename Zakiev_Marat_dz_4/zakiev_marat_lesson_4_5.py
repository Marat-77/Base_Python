# zakiev_marat_lesson_4_5
# ########################################! my_utils.py
# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
#

def main():
    # print(sys.argv)
    # можно вводить несколько параметров через пробел: usd eur uah byn kzt cny jpy
    param = sys.argv[1:]
    for arg in param:
        cur_val, _, _, cur_date = cur(arg)
        print(f'{round(cur_val, 2)}, {cur_date}')


if __name__ == '__main__':
    import sys
    from my_utils import currency_rates as cur
    main()
# надо будет еще разобраться с import argparse и документированием аргументов скрипта
# https://jenyay.net/Programming/Argparse
