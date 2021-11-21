# /Zakiev_Marat_dz_10/zakiev_marat_lesson_10_2.py
# zakiev_marat_lesson_10_2
#
# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

class Clothes:
    def __init__(self, name: str, param: int):
        self.name = name
        self.param = param

    @property
    def expenditure(self):
        return f'расход ткани составляет: {round(self.size / 6.5 + 0.5, 2) + round(self.height * 2 + 0.5, 2)}'


class Coat(Clothes):
    def __init__(self, name, param):
        super().__init__(name, param)
        self.size = self.param

    # @property
    def expenditure(self):
        return f'расход ткани на {self.name} составляет: {round(self.size / 6.5 + 0.5, 2)}'


class Suit(Clothes):
    def __init__(self, name, param):
        super().__init__(name, param)
        self.height = self.param

    # @property
    def expenditure(self):
        return f'расход ткани на {self.name} составляет: {round(self.height * 2 + 0.5, 2)}'


def main():
    print()
    black_coat = Coat('черное пальто', 56)
    office_suit = Suit('офисный костюм', 174)
    print(black_coat.expenditure())
    print(office_suit.expenditure())


if __name__ == '__main__':
    main()
