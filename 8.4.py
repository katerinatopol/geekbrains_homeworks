"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
from time import sleep


class Storage:
    def __init__(self, name, capacity_in_units):
        self.name = name
        self.capacity_in_units = capacity_in_units
        self.list_obj = []

    def store(self, obj):
        if self.capacity_in_units == 0:
            return 'склад полон, выберете другой'
        else:
            self.list_obj.append(obj)
            self.capacity_in_units -= 1
            return 'объект хранится на складе'

    def take_away(self, obj):
        self.list_obj.remove(obj)
        self.capacity_in_units += 1
        return 'объект забрали со склада'

    def auditor(self):
        return f'На складе хранятся: {self.list_obj}. Осталось свободных мест: {self.capacity_in_units}'


class OfficeEquipment:
    def __init__(self, model, year, condition):
        self.model = model
        self.year = year
        self.condition = condition
        self.status = 'free'

    def to_fix(self):
        self.condition += 30
        sleep(5)
        print('починился')

    def be_kept(self, storage):
        storage.store(self)
        self.status = 'be kept'
        return f'{self.model} хранится на складе {storage.name}'

    def take_free(self, storage):
        storage.take_away(self)
        self.status = 'free'
        return f'{self.model} забрали со склада'


class Printer(OfficeEquipment):
    def print(self):
        if self.condition < 50:
            print('Сломался. Ждите.')
            self.to_fix()
        self.condition -= 1
        print('идет печать, ждите')
        sleep(5)
        return 'Напечатал'



class Scanner(OfficeEquipment):
    def scan(self):
        if self.condition < 30:
            print('Сломался. Ждите.')
        self.condition -= 1
        return 'идет сканирование, ждите', sleep(5)


class Xerox(OfficeEquipment):
    def copy(self):
        if self.condition < 10:
            print('Сломался. Ждите.')

        self.condition -= 1
        return 'идет копирование, ждите', sleep(5)


storage_1 = Storage('первый склад', 4)
printer_1 = Printer('simple', 2020, 52)
print(printer_1.status)
print(printer_1.be_kept(storage_1))
print(printer_1.status)
print(printer_1.take_free(storage_1))
print(printer_1.status)
print(printer_1.print())
print(printer_1.print())
print(printer_1.print())
print(printer_1.print())
print(printer_1.print())
