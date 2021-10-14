# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# проверка введенных данных
duration = ''
while not duration.isdigit():
    duration = input('Введите продолжительность периода в секундах (Например: 45613216): ')
print(duration, 'сек.')
duration = int(duration)
# создаем список и добавляем первый элемент - секунды
list_duration = [duration % 60]
my_duration_str = '{} сек.'.format(list_duration[0])
days_str = ''  # создадим пустую строку для варианта без годов
if duration >= 60:
    # минуты
    duration = duration // 60  # отсекли секунды
    list_duration.append(duration % 60)  # добавление минут в список [1]
    new_str = '{} мин.'.format(list_duration[1])
    my_duration_str = f'{new_str} {my_duration_str}'
    if duration >= 60:
        # часы
        duration = duration // 60  # отсекли минуты
        list_duration.append(duration % 24)  # добавление часов в список [2]
        new_str = '{} час.'.format(list_duration[2])
        my_duration_str = f'{new_str} {my_duration_str}'
        if duration >= 24:
            # дни
            duration = duration // 24  # отсекли часы
            duration_days = duration
            list_duration.append(duration % 365)  # добавление дней в список [3]
            new_str = '{} дн.'.format(list_duration[3])
            days_str = f'{duration_days} дн. {my_duration_str}'
            my_duration_str = f'{new_str} {my_duration_str}'
            if duration >= 365:
                duration = duration // 365  # отсекли дни
                list_duration.append(duration)  # добавление годов в список [4]
                new_str = '{} г.'.format(list_duration[4])
                my_duration_str = f'{new_str} {my_duration_str}'

print('-' * 30)

if len(list_duration) > 4:
    print(days_str)  # вывод варианта без годов
    print('или')
    print(my_duration_str)  # варианта с годами
else:
    print(my_duration_str)  # тут годы не нужны
# well done!

# для проверки работы кода можно сделать цикл
# for i in range(1, 31536002):
# duration = i
# 31536000 c - это 365 дней или 1 год
# еще как вариант: создать список с ключевыми (критичными) значениями:
# [0, 1, 59, 60, 61, 3599, 3600, 3601, 86399, 86400, 86401, 31535999, 31536000, 31536001]
# и перебрать варианты duration из этого списка
