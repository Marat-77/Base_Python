# Урок 1. Задание 2.b
# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.

# прогнать через цикл от 1 до 1000 с шагом 2 и
# возвести в 3 степень и добавить в список "cube_odd_numbers"
cube_odd_numbers = []  # приготовим пустой список для кубов нечетных чисел
for mz_number in range(1, 1000, 2):
    mz_number = mz_number ** 3  # возведение в 3 степень
    cube_odd_numbers.append(mz_number)  # добавление в список

# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
seventeen_cube_odd = []
for i in cube_odd_numbers:
    i += 17
    seventeen_cube_odd.append(i)  # добавление в список

j_sum_seventeen_seven = 0
for j in seventeen_cube_odd:
    dec_j = 0
    j_seven = j
    while j > 0:
        dec_j = dec_j + j % 10
        j //= 10
    if dec_j % 7 == 0:
        j_sum_seventeen_seven = j_sum_seventeen_seven + j_seven

# вывод результата
print('b. Сумма чисел из списка (кубов нечетных чисел +17), сумма цифр которых делится нацело на 7:')
print(j_sum_seventeen_seven)

# это задание делал после 2.c - было проще и уже не так интересно, но полезно.
