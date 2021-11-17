# /Zakiev_Marat_dz_9/zakiev_marat_lesson_9_2.py
# zakiev_marat_lesson_9_2

# -------------------------------------------------------------------------------------------
# 2. Реализовать класс Road (дорога).
# - определить атрибуты: length (длина), width (ширина);
# - значения атрибутов должны передаваться при создании экземпляра класса;
# - атрибуты сделать защищёнными;
# - определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# - использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# - проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
# -------------------------------------------------------------------------------------------
#
# mass = length * width * mass_per_one * depth


class Road:
    def __init__(self, length, width):
        self._leght = length
        self._width = width

    def estimate(self, depth):
        mass_per_one = 25  # удельный вес асфальта на 1 кв.м толщиной 1 см.
        mass = self._leght * self._width * mass_per_one * depth
        return f'{mass//1000} т.'


# длина участка дороги (м):
length_one = 5000
# ширина (м):
width_one = 20
# толщина слоя (см):
depth_one = 5
new_road = Road(length_one, width_one)
result = new_road.estimate(depth_one)
print(result)
#