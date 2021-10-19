# Урок 1. Задание 3.
# 3. Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

# работает не только  до 100 - можно прописать любое число
percent_declination_list = ['а', 'ов']  # список вариаций окончания
one_percent_speak = 'процент'  # вариант для 1 и основа для остальных
for percent in range(1, 101):
    if percent > 10 and percent % 100 in range(11, 15):
        percent_speak = f'{percent} {one_percent_speak}{percent_declination_list[1]}'
        # Вывести эту фразу на экран отдельной строкой:
        print(percent_speak)
    elif percent % 10 == 1:
        percent_speak = f'{percent} {one_percent_speak}'
        # Вывести эту фразу на экран отдельной строкой:
        print(percent_speak)
    elif 1 < percent % 10 < 5:
        percent_speak = f'{percent} {one_percent_speak}{percent_declination_list[0]}'
        # Вывести эту фразу на экран отдельной строкой:
        print(percent_speak)
    else:
        percent_speak = f'{percent} {one_percent_speak}{percent_declination_list[1]}'
        # Вывести эту фразу на экран отдельной строкой:
        print(percent_speak)

print('_' * 19)
# вариант покороче
print('вариант без списка:')
# в этом варианте еще и максимум увеличил до 1000
for percent in range(1, 1001):
    if percent > 10 and percent % 100 in range(11, 15):
        print(f'{percent} процентов')
    elif percent % 10 == 1:
        print(f'{percent} процент')
    elif 1 < percent % 10 < 5:
        print(f'{percent} процента')
    else:
        print(f'{percent} процентов')

# исправил: числа от 11 до 20 должны быть "процентов"
