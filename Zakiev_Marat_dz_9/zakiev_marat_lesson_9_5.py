# /Zakiev_Marat_dz_9/zakiev_marat_lesson_9_5.py
# zakiev_marat_lesson_9_5

# -------------------------------------------------------------------------------------------
# 5. Реализовать класс Stationery (канцелярская принадлежность).
# - определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# - создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# - в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# - создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
# -------------------------------------------------------------------------------------------
#

class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки "{self.title}"'


class Pen(Stationery):
    def draw(self):
        return f'ручка "{self.title}": запуск отрисовки'


class Pencil(Stationery):
    def draw(self):
        return f'карандаш "{self.title}": запуск отрисовки'


class Handle(Stationery):
    def draw(self):
        return f'маркер "{self.title}": запуск отрисовки'


#
brush = Stationery('кисть')
print(brush.draw())
#
red_pen = Pen('красная ручка')
print(red_pen.draw())
#
pencil = Pencil('карандаш')
print(pencil.draw())
#
yellow_handle = Handle('желтый маркер')
print(yellow_handle.draw())
#
