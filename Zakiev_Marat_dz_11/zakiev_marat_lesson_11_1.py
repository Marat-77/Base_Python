# /Zakiev_Marat_dz_11/zakiev_marat_lesson_11_1.py
# zakiev_marat_lesson_11_1
# -------------------------------------------------------------------------------------------
# 1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
# -------------------------------------------------------------------------------------------

import re


class Date:
    def __init__(self, input_date):
        self.inp_date = input_date
        self.out_date = Date.validator(self.inp_date, show_input=False)
        if self.out_date:
            self.day, self.month, self.year = self.out_date
            self.out = f'{self.day:02}.{self.month:02}.{self.year}'
            self.out_list = [self.day, self.month, self.year]
        else:
            self.out = f'{self.inp_date} - Введенные данные некорректны, введите дату в формате «день-месяц-год»'

    def __str__(self):
        # это выводим при выводе print(объект_Класса)
        return self.out

    @classmethod
    def extract(cls, input_date):
        return cls(input_date)

    @staticmethod
    def bissextus(year):
        # високосный год
        # год, номер которого кратен 400, — високосный;
        # остальные годы, номер которых кратен 100, — невисокосные (например, годы 1800, 1900, 2100, 2200, 2300);
        # остальные годы, номер которых кратен 4, — високосные.
        # все остальные годы — невисокосные.
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    @staticmethod
    def test_day(input_date, re_day, re_month, re_year, n, show_input):
        if re_day not in range(1, n):
            if show_input:
                return input_date, False
            else:
                return False
        else:
            return re_day, re_month, re_year

    @staticmethod
    def validator(input_date, show_input=True):
        RE_DATE = re.compile(r'(^\d{0,2})-(\d{0,2})-(\d*)')
        re_out = RE_DATE.findall(input_date)
        if not re_out:
            if show_input:
                return input_date, False
            else:
                return False
        else:
            re_out = re_out[0]
            re_day, re_month, re_year = re_out
            re_day = int(re_day)
            re_month = int(re_month)
            re_year = int(re_year)
            if re_month > 12:
                if show_input:
                    return input_date, False
                else:
                    return False
            else:
                if re_month in (1, 3, 5, 7, 8, 10, 12):
                    n = 32
                    return Date.test_day(input_date, re_day, re_month, re_year, n, show_input)
                elif re_month in (4, 6, 9, 11):
                    n = 31
                    return Date.test_day(input_date, re_day, re_month, re_year, n, show_input)
                elif re_month == 2:
                    if Date.bissextus(re_year):
                        n = 30
                        return Date.test_day(input_date, re_day, re_month, re_year, n, show_input)
                    else:
                        n = 29
                        return Date.test_day(input_date, re_day, re_month, re_year, n, show_input)


def main():
    print('-' * 30)
    # проверка - високосный год?
    test_year = 904
    print(f'(staticmethod) Високосный год {test_year}?')
    print(Date.bissextus(test_year))
    print('-' * 30)
    #
    # =====================================================
    real_date = '29-02-2020'
    print(f'(staticmethod) Преобразуем {real_date}:')
    print(Date.validator(real_date))
    for i in Date.validator(real_date):
        print(f'{i} - {type(i)}')
    print('-' * 30)
    # объект класса Date
    my_obj_date = Date(real_date)
    print('my_obj_date - объект класса Date:')
    print(my_obj_date)
    print('-' * 30)
    #
    great_date = '9-5-1945'
    print(f'(staticmethod) Преобразуем {great_date}:')
    print(Date.validator(great_date))
    my_obj_great_date = Date(great_date)
    print('объект класса Date:')
    print(my_obj_great_date)
    print('-' * 30)
    # classmethod
    print('classmethod:')
    y_mmm = Date.extract('09-09-2019')
    print(y_mmm)
    #
    print()
    print('#' * 40)
    wrong_date = '41-24-2021'
    print(f'(staticmethod) Преобразуем {wrong_date}:')
    print(Date.validator(wrong_date))
    #
    print('-' * 30)
    my_obj_wrong_date = Date(wrong_date)
    print('my_obj_wrong_date - объект класса Date:')
    print(my_obj_wrong_date)
    print('#' * 40)


if __name__ == '__main__':
    main()

# .
