# /Zakiev_Marat_dz_11/zakiev_marat_lesson_11_2.py
# zakiev_marat_lesson_11_2
# -------------------------------------------------------------------------------------------
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
# -------------------------------------------------------------------------------------------

class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text


def my_divide(x, y):
    if y == 0:
        raise MyZeroDivisionError(f'ОШИБКА: {x}/{y} - Деление на "0" невозможно!')
    return x / y


def main():
    print(my_divide(8, 2))
    # ######################################
    # print(my_divide(5, 0))  # ZeroDivisionError: division by zero
    # ######################################
    # try:
    #     my_divide(5, 0)
    # except ZeroDivisionError as e:
    #     print(e)  # division by zero
    # ######################################
    try:
        my_divide(5, 0)
    except MyZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    main()

#
