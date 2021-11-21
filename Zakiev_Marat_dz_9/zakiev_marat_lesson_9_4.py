# /Zakiev_Marat_dz_9/zakiev_marat_lesson_9_4.py
# zakiev_marat_lesson_9_4

# -------------------------------------------------------------------------------------------
# 4. Реализуйте базовый класс Car.
# - у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# -------------------------------------------------------------------------------------------
#

class Car:
    def __init__(self, color: str, name: str, is_police: bool = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        return f'{self.name} набрал скорость {self.speed}км/ч'

    def stop(self):
        self.speed = 0
        return f'{self.name} остановился'

    def turn(self, direction: str):
        if direction == 'right' and self.speed > 0:
            return f'{self.name} повернул направо'
        elif direction == 'left' and self.speed > 0:
            return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Скорость {self.name} = {self.speed}км/ч'


class TownCar(Car):
    def show_speed(self):
        max_speed = 60
        if self.speed > max_speed:
            return f'{self.name} превышает скорость на {self.speed - max_speed}км/ч'
        else:
            return f'Скорость {self.name} = {self.speed}км/ч'


class WorkCar(Car):
    def show_speed(self):
        max_speed = 40
        if self.speed > max_speed:
            return f'{self.name} превышает скорость на {self.speed - max_speed}км/ч'
        else:
            return f'Скорость {self.name} = {self.speed}км/ч'


#
one_car = Car('black', 'Honda')
print(one_car.go(100))
print(one_car.show_speed())
print(one_car.turn('right'))
print(one_car.turn('left'))
print(one_car.is_police)
#
print('_' * 20)
bus = TownCar('yellow', 'Нефаз')
print(bus.go(20))
print(bus.show_speed())
print(bus.turn('right'))
print(bus.turn('left'))
print(bus.go(60))
print(bus.show_speed())
print(bus.go(65))
print(bus.show_speed())
print(bus.is_police)
#
print('_' * 20)
kamaz = WorkCar('red', 'Камаз')
print(kamaz.go(20))
print(kamaz.show_speed())
print(kamaz.turn('right'))
print(kamaz.turn('left'))
print(kamaz.go(40))
print(kamaz.show_speed())
print(kamaz.go(65))
print(kamaz.show_speed())
print(kamaz.is_police)
#
print('_' * 20)
police_car = Car('black', 'Ford', True)
print(police_car.go(80))
print(police_car.show_speed())
print(police_car.turn('right'))
print(police_car.turn('left'))
print(police_car.is_police)
#
#
