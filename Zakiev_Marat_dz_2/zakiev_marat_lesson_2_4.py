# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на
# экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов
# списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

employees = ['инженер-конструктор Игорь',
             'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй',
             'директор аэлита',
             'НаЧальник производственного отдела СаЛават',
             'оператор МАШИННОГО ДОЕНИЯ АЛЕВТИНА',
             'ОХранник Петр']
print(employees)
for employee in employees:
    print(f'Привет, {(employee.split()[-1]).title()}!')
# for employee in employees - перебирает каждый элемент (employee) из списка (employees)
# employee.split() - делит строку (employee) по разделителю (по умолчанию - пробел)
# [-1] - берет последний элемент из разделенных
# .title() - "причёсываем" регистр. (Можно использовать и capitalize() т.к. выводится только одно слово)

# well done!
