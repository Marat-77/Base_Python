# zakiev_marat_lesson_4_3
# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
#

import datetime
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
    # print(f'!!!---- str_a{str_a}')
    # print(f'len str_={len(str_a)}')
    # print(f'===========-------------index_a---{index_a}')
    # print(text[index_a:])
    # index_a += index_a + len(str_a) - 1  # index_a + > +1
    index_a += len(str_a)  # index_a + > +1
    # index_a += (text[index_a:]).find('>') + 1  # index_a + > +1
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
        help_charcode(input_text)  # функция показывает подсказку по кодам валют !!!!!!!
        currency = input('Введите код валюты (например, USD, EUR, GBP, ...): ')
        currency = currency.upper()
        # --------------*******************************************************--------------
        if input_text.count(currency + '</CharCode>') == 0:
            # print(None)
            # return_none = None
            return None
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
            response_date = find_value_str(input_text, '<ValCurs Date="', '"')
            # - находим необходимый участок строки
            response_day = int(response_date[:2])
            response_month = int(response_date[3:5])
            response_year = int(response_date[-4:])
            cur_date = datetime.date(response_year, response_month, response_day)
            # print(type(cur_date))
            date_str_currency_value = f'{cur_date}: {str_currency_value} руб.'
            print(date_str_currency_value)
            # return str_currency_value, float_currency_value, round_currency_value, cur_date
            return float_currency_value
        # print('<<<<<<<<<< - currency_rates - >>>>>>>>>>')
        # --------------*******************************************************--------------
        # Date="29.10.2021"
        # 29.10.2021
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


if __name__ == '__main__':
    currency_rates()
