# /Zakiev_Marat_dz_9/zakiev_marat_lesson_9_3.py
# zakiev_marat_lesson_9_3

# -------------------------------------------------------------------------------------------
# 3. Реализовать базовый класс Worker (работник).
# - определить атрибуты: name, surname, position (должность), income (доход);
# - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# - создать класс Position (должность) на базе класса Worker;
# - в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# - проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
# -------------------------------------------------------------------------------------------
#

class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        dict_income = {'wage': wage, 'bonus': bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict_income  # protected


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        # total_income = round(wage + bonus, 2)
        # wage, bonus - values словаря self._income
        total_income = round(sum(self._income.values()), 2)
        return total_income


urri = Position('Urri', 'Catcher', 'охотник за Электроником', 100000.456, 50000.36)
print(type(urri))

print(urri.get_full_name())
print(urri.position)
print(urri.get_total_income())
