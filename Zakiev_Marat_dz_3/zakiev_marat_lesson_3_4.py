# draft_zakiev_marat_lesson_3_4.py
# 4. *(вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания
# и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

# mmmmmm #     "А": {
# surname_letter:
#        name_letter: ['Name Surname']
# #         "П": ["Петр Алексеев"]
# mmmm
# employee in employees
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# def thesaurus_adv(employees: list) -> dict:
def thesaurus_adv(employees: str):
    print('*** Функция thesaurus_adv ***')
    # print(f'f1входящая строка = {employees}/ тип {type(employees)}')
    employees = employees.strip(',')  # удаляет запятую слева и справа строки
    employees = employees.split(',')  # разбиваем полученную строку по ',' и получаем список employees
    print(f'f2 список employees = входящая строка.split(",") = {employees}/ тип {type(employees)}')
    print('#' * 45)
    # #####################################################################################################
    for val_employee in employees:
        print(f'\n---0001!---val_employee= "{val_employee}"\n in employees{employees}')
        if not val_employee.isspace():
            # - исключаем непечатные символы, избежим ошибки в случае если был введен только пробел/ы.
            # имя из полученного списка с удаленными пробелами (слева и справа) и с заглавной:
            val_employee = val_employee.strip().title()
            employee_key = val_employee[0]  # из первого элемента строки (имени) создаем ключ
            # print(f'employee_key = {employee_key} --- ***************************')
            surname_letter = (val_employee.split()[-1])[0]  # --- *********************************
            # print(f'surname_letter = {surname_letter} --- ***************************')
            # --------------------------------------------------------------------------------------------
            if dict_surname.get(surname_letter) is None:
                print(f'если ключа {surname_letter} - Буква_фамилии в словаре НЕТ:')
                # если ключа surname_letter в словаре ФАМИЛИЙ нет:
                dict_surname[surname_letter] = {employee_key: [val_employee]}  # создаем ключ и значение !!!!!!!!!!!!!
                # ключ = Буква_фамилии, значение = словарь {Буква_имени: Имя Фамилия}
                # print(f'создаем ключ Буква_фамилии ({surname_letter}) и')
                # print(f'значение-словарь ({employee_key}: {val_employee})')
                # print('dict_surname -выводим dict_surname-----------------------!')
                # выводим dict_surname:
                print(dict_surname)
                # => {'С': {'И': 'Иван Сергеев'}}
            else:
                print(f'иначе (такой ключ {surname_letter} ЕСТЬ):')
                # получаем значение этого ключа:
                print('получаем значение этого ключа:')
                print(dict_surname.get(surname_letter))
                # => получаем значение этого ключа:
                # => {'И': 'Иван Сергеев'}
                #
                if (dict_surname.get(surname_letter)).get(employee_key) is None:
                    # если ключа employee_key в словаре И:[Имя Фамилия] нет:
                    dict_surname.get(surname_letter)[employee_key] = [val_employee]
                    # - записываем во вложенный словарь ключ "employee_key" (Буква_имени)
                    # и значение [val_employee] - [Имя Фамилия]

                    print('dict_surname -выводим dict_surname-----------------------!')
                    # выводим dict_surname:
                    print(dict_surname)
                    # => {'С': {'И': 'Иван Сергеев'}}
                else:
                    print(f'если ключ {employee_key} - Буква_имени! в словаре ЕСТЬ:')
                    # если ключа employee_key в словаре И:[Имя Фамилия] нет:
                    # => значение ключа И во вложенном словаре:
                    # => ['Иван Сергеев']
                    dict_surname[surname_letter] = {
                        employee_key: (dict_surname.get(surname_letter)).get(employee_key) + [val_employee]
                    }
                    # (dict_surname.get(surname_letter)).get(employee_key)
                    # - это значение(список) вложенного словаря = ['Иван Сергеев']
                    # dict_surname[surname_letter] = {(dict_surname.get(surname_letter))[employee_key] = val_employee}
                    # (dict_surname.get(surname_letter))[employee_key] = val_employee
                    # dict_surname[surname_letter] = {employee_key: [val_employee]}  # создаем ключ и значение !!!!!!!!
                    print(f'значение ключа {employee_key} во вложенном словаре:')
                    # dict_surname[surname_letter] = {employee_key: val_employee}  # создаем ключ и значение !!!!!!-???
                    print('dict_surname -выводим dict_surname-----------------------!')
                    # выводим dict_surname:
                    print(dict_surname)

            # --------------------------------------------------------------------------------------------
            # --------------------------------------------------------------------------------------------
    return dict_employees  # выдаём полученный словарь
    # ########################################################################################################



def main():
    print('--- function main() ---')
    # dict_employees = dict()  # ======================================== СЛОВАРЬ - СОТРУДНИКИ ========================!
    while True:
        print('--- main menu ---')
        user_choice = input('1 - Добавить сотрудника/ков\n2 - Посмотреть полученный словарь\n0 - Выход\nВведите: ')
        print(f'\nВы выбрали: {user_choice}')
        if user_choice == '1':
            print('Добавить сотрудника/ков:')
            input_employees1 = 'Иван Сергеев, Инна Серова, Петр Алексеев, Илья Иванов, Анна Савельева.'  # delete after test1 ------------------------------
            print(f'input_employees1 = {input_employees1}')  # delete after test1 ------------------------------
            print(f'тип input_employees1 = {type(input_employees1)}')  # delete after test1 ------------------------------
            # ############################################################################ ВЕРНУТЬ ПОСЛЕ ТЕСТА
            # input_employees = input(
            #     'Введите Имя и Фамилию сотрудника или несколько сотрудников через запятую\n'
            #     '(например: Иван Петров, Сергей Скворцов): '
            # )
            # print(f'Вы ввели: {input_employees}')
            # print(f'тип {type(input_employees)}')
            # thesaurus_adv(input_employees.split(','))
            # ############################################################################ ВЕРНУТЬ ПОСЛЕ ТЕСТА
            # thesaurus_adv1(input_employees1.split(','))  # delete after test1 ------------------------------
            thesaurus_adv(input_employees1)  # delete after test1 ------------------------------
        elif user_choice == '2':
            print('Посмотреть полученный словарь')
            print(dict_employees)
            print('----- Словарь построчно:')
            for keys, values in dict_surname.items():
                print(f'{keys}: {values}')
            # for keys, values in dict_names.items():
            #     print(f'{keys}: {values}')  # выводим полученный словарь построчно
            print('------ конец словаря ------')
        elif user_choice == '0':
            print('Вы вышли из программы')
            break
        else:
            print(f'Вы ввели: {user_choice} - в этом меню не используется')


if __name__ == '__main__':
    dict_surname = dict()  # ======================================== СЛОВАРЬ ФАМИЛИИ СОТРУДНИКОВ ====================!
    dict_employees = dict()  # ======================================== СЛОВАРЬ - СОТРУДНИКИ =========================!
    # ?????--------------------------------------- Нужен ли словарь "dict_employees"???????????????????????????????????
    main()

