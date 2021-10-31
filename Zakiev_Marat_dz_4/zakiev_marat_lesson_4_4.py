# zakiev_marat_lesson_4_4.
# ########################################! my_utils.py
# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.
#

# my_utils
import my_utils
from my_utils import currency_rates as cur


def exchange(cash: float, curencycode: str):
    a, b, c, d = cur(curencycode)
    exchange_date = d.strftime('%d.%m.%Y')
    result_exchange = f'{exchange_date}: {cash} {c} = {round((cash * a / b), 2)} RUB'
    return result_exchange


def main():
    x = my_utils.currency_rates('XDR')  # используем import draft_utils
    y = cur('eur')  # используем from draft_utils import currency_rates as cur
    print(x)
    print(y)
    z = cur('sfg')
    print(z)
    print('-' * 50)  # ------------------------------------ test exchange() -------
    # exchange
    print('exchange')
    # 1 UAH = 26.8152 / 10 RUB
    # 1 KZT = 16.494 / 100 RUB
    input_money = 8710
    input_cur = 'uah'
    print(exchange(input_money, input_cur))
    # input_money = 12800
    # input_cur = 'KZT'
    # print(exchange(input_money, input_cur))
    # input_money = 87.10
    # input_cur = 'byn'
    # print(exchange(input_money, input_cur))
    # input_money = 0.1
    # input_cur = 'eur'
    # print(exchange(input_money, input_cur))


if __name__ == '__main__':
    main()

# =============== HELP ===============
# AUD - Австралийский доллар
# AZN - Азербайджанский манат
# GBP - Фунт стерлингов Соединенного королевства
# AMD - Армянских драмов
# BYN - Белорусский рубль
# BGN - Болгарский лев
# BRL - Бразильский реал
# HUF - Венгерских форинтов
# HKD - Гонконгских долларов
# DKK - Датская крона
# USD - Доллар США
# EUR - Евро
# INR - Индийских рупий
# KZT - Казахстанских тенге
# CAD - Канадский доллар
# KGS - Киргизских сомов
# CNY - Китайский юань
# MDL - Молдавских леев
# NOK - Норвежских крон
# PLN - Польский злотый
# RON - Румынский лей
# XDR - СДР (специальные права заимствования)
# SGD - Сингапурский доллар
# TJS - Таджикских сомони
# TRY - Турецких лир
# TMT - Новый туркменский манат
# UZS - Узбекских сумов
# UAH - Украинских гривен
# CZK - Чешских крон
# SEK - Шведских крон
# CHF - Швейцарский франк
# ZAR - Южноафриканских рэндов
# KRW - Вон Республики Корея
# JPY - Японских иен
# ============= END HELP =============
