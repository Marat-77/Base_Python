# my_utils
# my_utils for zakiev_marat_lesson_4_4 & zakiev_marat_lesson_4_4

# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.
#

# ################################################################################################################

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
    index_a += len(str_a)  # index_a + len(str_a)
    text_b = text[index_a:]
    if str_b == '':
        value_str = text[index_a:]
    else:
        index_b = text_b.find(str_b)  # index_b
        index_b += index_a
        value_str = text[index_a:index_b]
    return value_str


def currency_rates(currency: str):
    """
    Function get currency and return tuple[Currency_Value: float, Currency_Nominal: int, Currency_CharCode: str, date]
     from CBR (Bank of Russia)
    :param currency: Currency_CharCode: str
    :return: Currency_Value: float, Currency_Nominal: int, Currency_CharCode: str, date
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', timeout=5)
    if response.status_code == 200:
        input_text = response.text
        currency = currency.upper()
        # --------------*******************************************************--------------
        if input_text.count(currency + '</CharCode>') == 0:
            return None
        else:
            x = currency + '</CharCode>'
            x_text = find_value_str(input_text, x, '</Valute>')  # находим необходимый участок строки
            currency_nominal = find_value_str(x_text, '<Nominal>', '</Nominal>')  # находим номинал
            currency_value = find_value_str(x_text, '<Value>', '</Value>')  # находим значение
            float_currency_value = float(currency_value.replace(',', '.'))
            # - меняем запятую на точку и приводим к типу float
            response_date = find_value_str(input_text, '<ValCurs Date="', '"')
            # - находим необходимый участок строки
            response_day = int(response_date[:2])
            response_month = int(response_date[3:5])
            response_year = int(response_date[-4:])
            cur_date = datetime.date(response_year, response_month, response_day)
            int_currency_nominal = int(currency_nominal)
            return float_currency_value, int_currency_nominal, currency, cur_date
        # --------------*******************************************************--------------
    elif response.status_code == 404:
        print('Не найден.')


if __name__ == '__main__':
    my_x = currency_rates('usd')
    print(f'test: {my_x}')
else:
    print()
    # print("This is lib")
# ################################################################################################################
