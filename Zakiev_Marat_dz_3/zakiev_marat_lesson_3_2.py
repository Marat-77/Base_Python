# zakiev_marat_lesson_3_2
# 2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы
#  — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


# объявление функции
def num_translate(en_num):
    """
    Function translate English numerals (from zero to ten) into Russian
    :param en_num: str
    :return: str
    """
    eng_rus = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return eng_rus.get(en_num)


print('Программа перевода английских числительных (от 0 до 10) на русский язык')
print('Program for translate English numerals (from zero to ten) into Russian')
print('*' * 73)

input_str = ''
while input_str != 'exit':
    # цикл работает пока пользователь не ввел exit
    input_str = input('Введите английское числительное (например: five)\n[для выхода введите "exit"]: ')
    if input_str == 'exit':
        # вывести сообщение если введен exit
        print('Вы вышли из программы')
    elif input_str.istitle():
        # Если не exit, то если введенная строка input_str начинается с заглавной буквы
        if num_translate(input_str.lower()) is None:
            # если в словаре нет такого ключа и функция num_translate() выдаст None
            # то выводим результат без изменения регистра
            print(num_translate(input_str))
        else:
            # выводим результат так же с заглавной буквы
            print(num_translate(input_str.lower()).title())
    else:
        # Иначе (если не с заглавной), то выводим результат функции num_translate()
        print(num_translate(input_str))  # выводим перевод
