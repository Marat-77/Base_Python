# zakiev_marat_lesson_4_2
# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
#

# Можно ли, используя только методы класса str, решить поставленную задачу?
# - Да. у меня получилось

# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# - для Decimal необходимо будет использовать import Decimal

import requests


def find_value_str(text: str, str_a: str, str_b: str = '') -> str:
    """
    Function return string between str_a and str_b from text
    :param text: str
    :param str_a: str
    :param str_b: str
    :return: str
    """
    index_a = text.find(str_a)  # index_a
    index_a += (text[index_a:]).find('>') + 1  # index_a + > +1
    text_b = text[index_a:]
    if str_b == '':
        value_str = text[index_a:]
    else:
        index_b = text_b.find(str_b)  # index_b
        index_b += index_a
        value_str = text[index_a:index_b]
    return value_str


def currency_rates():
    """
    Function get from user currency code and print currency exchange rate from CBR (Bank of Russia)
    :return: float
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', timeout=5)
    if response.status_code == 200:
        input_text = response.text
        currency = input('Введите код валюты (например, USD, EUR, GBP, ...)/или help для подсказки: ')
        currency = currency.upper()
        # --------------*******************************************************--------------
        if currency == 'HELP':
            help_charcode(response.text)  # функция показывает подсказку по кодам валют !!!!!!!
        elif input_text.count(currency + '</CharCode>') == 0:
            print(None)
        else:
            x = currency + '</CharCode>'
            x_text = find_value_str(input_text, x, '</Valute>')  # находим необходимый участок строки
            currency_nominal = find_value_str(x_text, '<Nominal>', '</Nominal>')  # находим номинал
            currency_value = find_value_str(x_text, '<Value>', '</Value>')  # находим значение
            float_currency_value = float(currency_value.replace(',', '.'))
            # - меняем запятую на точку и приводим к типу float
            round_currency_value = round(float_currency_value, 2)
            # значение котировки, округленное до сотых
            str_currency_value = f'{currency_nominal} {currency} = {round_currency_value} руб.'
            # - создаем строку необходимого вида
            # print(f'float={float_currency_value}|')
            # print(round_currency_value)
            print(str_currency_value)
            # return str_currency_value, float_currency_value, round_currency_value
            return float_currency_value
        print('<<<<<<<<<< - currency_rates - >>>>>>>>>>')
        # --------------*******************************************************--------------
    elif response.status_code == 404:
        print('Не найден.')


def help_charcode(input_text):
    print('=============== HELP ===============')
    # это HELP:
    while input_text != '</ValCurs>':
        charcode = find_value_str(input_text, '<CharCode>', '</CharCode>')
        name = find_value_str(input_text, '<Name>', '</Name>')
        print(f'{charcode} - {name}')
        finish_text = find_value_str(input_text, '</Valute>')
        input_text = finish_text
    print('============= END HELP =============')


def main():
    while True:
        print('\n----- основное меню: -----')
        user_choice = input(
            '1 - Посмотреть котировки валют\n0 - Выход\nВведите: '
        )
        print(f'\nВы выбрали: {user_choice}')
        if user_choice == '1':
            print('Просмотр котировок валют по курсу Банка России')
            # str_cur, float_cur, round_cur = currency_rates()
            # print(f'string: {str_cur}')
            # print(f'float: {float_cur}')
            # print(f'rounded: {round_cur}')
            currency_rates()
        elif user_choice == '0':
            print('Вы вышли из программы')
            break
        else:
            print(f'Вы ввели: {user_choice} - в этом меню не используется')


if __name__ == '__main__':
    main()
