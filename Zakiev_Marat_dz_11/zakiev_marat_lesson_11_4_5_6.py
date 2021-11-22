# /Zakiev_Marat_dz_11/zakiev_marat_lesson_11_4_5_6.py
# zakiev_marat_lesson_11_4_5_6
#
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
#

from functools import reduce


class Storehouse:
    def __init__(self, name: str, locality: str, post_address: str, geom_size: tuple):
        # self.__resources = []
        self.__assets = {}
        self.__name = name
        self.__locality = locality
        self.__post_address = post_address
        self.__full_size = reduce(lambda x, y: x * y, geom_size)
        self.__square = geom_size[0] * geom_size[1]

    def __str__(self):
        return f'склад "{self.__name}", адрес: {self.__locality}, {self.__post_address}, площадь: {self.__square}м2, ' \
               f'Объем:{self.__full_size}м3'

    # def прием на склад
    def receive_goods(self, goods, quantity: int = 1):
        print(f'Принимаем на склад {quantity}шт. "{goods}"')
        if self.__assets.get(goods) is None:
            self.__assets[goods] = quantity
        else:
            self.__assets[goods] = self.__assets.get(goods) + quantity
        print(f'Приняли на склад {quantity}шт. "{goods}"')
        print(f'"{goods}" на складе: {self.__assets.get(goods)}шт.')

    # def выдача со склада
    def transfer_goods(self, goods, destination, quantity: int = 1):
        print(f'\nОтгрузить {quantity}шт. "{goods}" на "{destination}".')
        if self.__assets.get(goods) is None or self.__assets.get(goods) == 0:
            print(f'"{goods}" на складе {self.__name} отсутствует')
        else:
            if quantity <= self.__assets.get(goods):
                self.__assets[goods] = self.__assets.get(goods) - quantity
                print(f'\nОтгружено {quantity}шт. "{goods}" на "{destination}"')
                print(f'"{goods}" на складе осталось {self.__assets.get(goods)}шт.')
            elif quantity > self.__assets.get(goods):
                print(f'На складе имеется только {self.__assets.get(goods)}шт. "{goods}"')
                quantity = self.__assets.get(goods)
                self.__assets[goods] = self.__assets.get(goods) - quantity
                print(f'\nОтгружено {quantity}шт. "{goods}" на "{destination}"')
                print(f'"{goods}" на складе осталось {self.__assets.get(goods)}шт.')

    def audit(self):
        for i, (k, v) in enumerate(self.__assets.items()):
            print(f'{v} шт."{k}"')
        # Хотел, но не успел реализовать суммирование объемов, масс и цен
        # выводить информацию о заполненности склада


class OfficeEquipment:
    def __init__(
            self, type_eq: str, brand_name: str, model: str, serial_number: str, size: tuple, gross_weight: float,
            price: float
    ):
        self.type_eq = type_eq
        self.brand_name = brand_name
        self.model = model
        self.serial_number = serial_number
        self.size = size
        self.gross_weight = gross_weight
        self.price = price

    def __repr__(self):
        out = (self.type_eq, self.brand_name, self.model, self.serial_number, self.size, self.gross_weight, self.price)
        return f'{out}'

    def __str__(self):
        return f'{self.type_eq} {self.brand_name} {self.model}, s/n: {self.serial_number}, размеры: {self.size}мм, ' \
               f'вес брутто: {self.gross_weight}кг, {self.price}руб.'


class Computer(OfficeEquipment):
    def __init__(
            self, brand_name: str, model: str, serial_number: str, size: tuple, gross_weight: float, price: float,
            operating_system: str, central_proc: str, ram_memory
    ):
        self.operating_system = operating_system
        self.central_proc = central_proc
        self.ram_memory = ram_memory
        super(Computer, self).__init__('ПК', brand_name, model, serial_number, size, gross_weight, price)

    def coding(self):
        print(f'{self.brand_name} {self.model} - можем питонить ;)')

    def web_serf(self):
        print(f'{self.brand_name} {self.model} - можем сёрфить интернет')


# Монитор
class Display(OfficeEquipment):
    def __init__(
            self, brand_name: str, model: str, serial_number: str, size: tuple, gross_weight: float, price: float,
            display_size: float, resolution: tuple
    ):
        self.display_size = display_size
        self.resolution = resolution
        super().__init__('Монитор', brand_name, model, serial_number, size, gross_weight, price)

    def show_screen(self):
        print(f'{self.brand_name} {self.model} может выводить изображение на экран')


# Принтер
class Printer(OfficeEquipment):
    def __init__(
            self, brand_name: str, model: str, serial_number: str, size: tuple, gross_weight: float, price: float,
            color_mode: str, print_technology: str, print_format: str
    ):
        self.color_mode = color_mode
        self.print_technology = print_technology
        self.print_format = print_format
        super().__init__('Принтер', brand_name, model, serial_number, size, gross_weight, price)

    def print_text(self):
        print(f'{self.brand_name} {self.model} может напечатать текст')

    def print_photo(self):
        print(f'{self.brand_name} {self.model} может напечатать фотографии')


# Сканер:
class ImageScanner(OfficeEquipment):
    def __init__(
            self, brand_name: str, model: str, serial_number: str, size: tuple, gross_weight: float, price: float,
            scan_format: str, film_scanner: bool = False
    ):
        self.scan_format = scan_format
        self.film_scanner = film_scanner
        super().__init__('Сканер', brand_name, model, serial_number, size, gross_weight, price)

    def scan_text(self):
        print(f'{self.brand_name} {self.model} может сканировать текст')

    def scan_photo(self):
        print(f'{self.brand_name} {self.model} может сканировать фотографии')


# Копир
class PhotoCopier(OfficeEquipment):
    def __init__(
            self, brand_name: str, model: str, serial_number: str, size: tuple, gross_weight: float, price: float,
            color_mode: str, print_technology: str, scan_format: str, print_format: str = 'as_scan_format'
    ):
        self.color_mode = color_mode
        self.print_technology = print_technology
        self.scan_format = scan_format
        if print_format == 'as_scan_format':
            self.print_format = scan_format
        else:
            self.print_format = print_format
        super().__init__('Копир', brand_name, model, serial_number, size, gross_weight, price)

    def copy_sheet(self):
        print(f'{self.brand_name} {self.model} может копировать лист')


if __name__ == '__main__':
    comp_01 = Computer('Dell', 'OptiPlex 3080 Micro', '9DJ3YH3', (218, 76, 223), 1.4, 30799.2, 'Linux',
                       'Intel Core i3', 'DDR4 8GB')
    # print(comp_01)
    comp_02 = Computer('Dell', 'Vostro 3888', '9DJ5YF5', (333, 194, 364), 12.8, 35198.4, 'Windows 10',
                       'Intel Core i3', 'DDR4 8GB')
    # print(comp_02)
    comp_03 = Computer('HP', 'Slim Desktop S01-pF1041ur', '4CE1280F55', (499, 196, 346), 6.2, 38310.4, 'Windows 10',
                       'Intel Core i5', 'DDR4 8GB')
    # print(comp_03)
    comp_04 = Computer('ASUS', 'ExpertCenter D500MA', 'L7P2CG000361317', (492, 232, 510), 6.3, 30958.4, 'Windows 10',
                       'Intel Pentium Gold', 'DDR4 8GB')
    # print(comp_04)
    printer_01 = Printer('HP', 'LaserJet Pro M15a', '5DF1340E42', (250, 406, 230), 5.2, 6740, 'color', 'laser', 'A4')
    # print(printer_01)

    # print(type(printer_01))  # <class '__main__.Printer'>

    # создаем склад:
    storehause_01 = Storehouse('Склад №1', 'Москва', 'Наметкина, д. 16', (25, 30, 8))
    print('\nСоздали склад:')
    print(storehause_01)

    print('_ ' * 30)
    # грузим на склад:
    print('\n1. грузим на склад:')
    storehause_01.receive_goods(printer_01)
    print('\n1. грузим на склад:')
    storehause_01.receive_goods(comp_01, 3)
    print('\n1. грузим на склад:')
    storehause_01.receive_goods(comp_02, 10)

    print('_ ' * 30)
    # отгружаем со склада:
    print('\n2. отгружаем со склада:')
    print(comp_01)
    storehause_01.transfer_goods(comp_01, 'Offline Shop 1')

    print('_ ' * 30)
    print('\n2 отгружаем со склада:')
    print(comp_02)
    storehause_01.transfer_goods(comp_02, 'Offline Shop 1', 3)

    print('_ ' * 30)
    print('\n2. отгружаем со склада:')
    print(comp_03)
    storehause_01.transfer_goods(comp_03, 'Offline Shop 2', 2)

    print('_ ' * 30)
    # грузим на склад:
    print('\n3. грузим на склад:')
    storehause_01.receive_goods(printer_01, 4)

    print('_ ' * 30)
    # отгружаем со склада:
    print('\n3. отгружаем со склада:')
    print(printer_01)
    storehause_01.transfer_goods(printer_01, 'New-iShop.ru', 10)

    print('_ ' * 30)
    # проверка склада:
    print('\nПроверка склада:')
    storehause_01.audit()

#
