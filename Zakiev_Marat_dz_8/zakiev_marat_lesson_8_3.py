# zakiev_marat_lesson_8_3

# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
#
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
from functools import wraps


def logger(verbosity=0):
    def _logger(func):
        @wraps(func)  # маскируем wrapper
        def wrapper(*args):
            result = func(*args)
            msg = f'{func.__name__}'
            if verbosity > 0:
                msg = f'{msg}({",".join(map(str, args))}: {type(*args)})'
            if verbosity > 1:
                msg = f'{msg} -> {result}'
            return msg
        return wrapper
    return _logger


@logger(verbosity=1)
def calc_cube(x):
    return x ** 3


def main():
    a = calc_cube(5)
    print(a)
    print(calc_cube.__name__)  # без маскировки = wrapper, с маскировкой (@wraps(func)) = calc_cube


if __name__ == '__main__':
    main()

# получаем:
# 0. без @logger:
# 125
# 1. если @logger:
# <function logger.<locals>._logger.<locals>.wrapper at 0x00000286711A0550>
# 2. если @logger(verbosity=0):
# calc_cube
# 3. если @logger(verbosity=1):
# calc_cube(5: <class 'int'>)
# 4. если @logger(verbosity=2):
# calc_cube(5: <class 'int'>) -> 125
