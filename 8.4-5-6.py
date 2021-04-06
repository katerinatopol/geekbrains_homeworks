"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod
from time import sleep


class Storage:
    list_storage = []

    def __init__(self, name, capacity_in_units):
        self.name = name
        self.capacity_in_units = capacity_in_units
        self.list_obj = []
        Storage.list_storage.append(self)

    def store(self, obj):
        if self.capacity_in_units == 0:
            return 'Склад полон, выберете другой.'
        else:
            self.list_obj.append(obj)
            self.capacity_in_units -= 1
            return f'{obj.model} теперь хранится на складе.'

    def take_away(self, obj):
        for i in self.list_obj:
            if i.model == obj.model:
                self.list_obj.remove(i)
        self.capacity_in_units += 1
        return 'Объект забрали со склада.'

    @staticmethod
    def short_auditor(storage):
        printer, scanner, xerox = 0, 0, 0
        print('На складе хранятся:')
        for elem in storage.list_obj:
            if isinstance(elem, Printer):
                printer += 1
            elif isinstance(elem, Scanner):
                scanner += 1
            elif isinstance(elem, Xerox):
                xerox += 1
        return f'{printer} принтеров\n{scanner} сканеров\n{xerox} ксероксов'

    @staticmethod
    def long_auditor(storage):
        print(f'На {storage.name} хранятся:')
        for ind, obj in enumerate(storage.list_obj, 1):
            print(f"{ind} {obj.__class__.__name__}: Модель {obj.model}, {obj.year} года выпуска")
        return f'Осталось свободных мест: {storage.capacity_in_units}'


class OfficeEquipment(ABC):
    list_office_equipment = []

    def __init__(self, model='NoName', year='NoInfo', condition=None):
        self.model = model
        self.year = year
        if condition == 'новый':
            self.condition = 100
        else:
            self.condition = 60
        self.status = 'free'

    @abstractmethod
    def use(self):
        pass

    def to_fix(self):
        self.condition += 30
        sleep(5)
        print('Починился.')

    def be_kept(self, storage):
        if self.status == 'be kept':
            return 'Объект уже на хранении'
        storage.store(self)
        self.status = 'be kept'
        return f'{self.model} хранится на складе {storage.name}'

    def take_free(self, storage):
        if self.status == 'free':
            return 'Объекта нет на складе'
        storage.take_away(self)
        self.status = 'free'
        return f'{self.model} забрали со склада'


class Printer(OfficeEquipment):
    def use(self):
        if self.condition < 50:
            print('Сломался. Ждите.')
            self.to_fix()
        self.condition -= 1
        print('идет печать, ждите')
        sleep(5)
        return 'Напечатал'


class Scanner(OfficeEquipment):
    def use(self):
        if self.condition < 30:
            print('Сломался. Ждите.')
            self.to_fix()
        self.condition -= 1
        print('идет сканирование, ждите')
        sleep(5)
        return 'Отсканировал'


class Xerox(OfficeEquipment):
    def use(self):
        if self.condition < 10:
            print('Сломался. Ждите.')
            self.to_fix()
        self.condition -= 1
        print('идет копирование, ждите')
        sleep(5)
        return 'Откопировал'


storage_1 = Storage('Первый склад', 4)
storage_2 = Storage('Второй склад', 100)
printer_1 = Printer('printer simple', 2020, 52)
xerox_1 = Xerox('xerox-1', 2010, 30)
scan_1 = Scanner('Y4UYN-scanner', 2009, 100)
printer_1.be_kept(storage_1)
xerox_1.be_kept(storage_1)
scan_1.be_kept(storage_1)
printer_2 = Printer('printer hard', 2015, 60)
xerox_2 = Xerox('xerox-2', 2000, 10)
scan_2 = Scanner('SUPER-scanner', 2020, 200)
printer_2.be_kept(storage_2)
xerox_2.be_kept(storage_2)
scan_2.be_kept(storage_2)


while True:
    user_answer = input('-----------------------------\nДобро пожаловать в программу СКЛАД. Что вы хотите сделать:\n'
                        '- добавить новый склад\n- отправить технику на склад\n- перемещать технику между складами\n'
                        '- отправиться на склад\n- завершить работу Q\nВведите ответ: ')
    if user_answer.lower() == 'добавить новый склад':
        print(f'-----------------------------\nДля возврата в главное меню введите -\nУ нашей компании есть склады: '
              f'{", ".join([i.name for i in Storage.list_storage])}.')
        while True:
            try:
                user_answer = input(f'Укажите информацию о новом складе: название, вместимость (введите через запятую): ')
                if user_answer == '-':
                    break
                name, capacity_in_units = user_answer.split(', ')
                capacity_in_units = int(capacity_in_units)
            except ValueError as err:
                print(f'Возникла ошибка({err}), проверьте корректность ввода')
            else:
                Storage(name, capacity_in_units)
                print(f'{name} зарегистрирован в системе.')

    elif user_answer.lower() == 'отправить технику на склад':
        while True:
            user_answer = input(f'-----------------------------\nДля возврата в главное меню введите -\n'
                                f'У нашей компании есть склады: {", ".join([i.name for i in Storage.list_storage])}.'
                                f'\nУкажите, на какой склад вы хотите отправить технику: ')
            if user_answer == '-':
                break
            else:
                if user_answer in [i.name for i in Storage.list_storage]:
                    working_storage = [el for el in Storage.list_storage if el.name == user_answer][0]
                    while True:
                        user_answer = input(f'-----------------------------\nОтправляем технику на {working_storage.name}.'
                                            f' Для отмены введите -\nКакой из видов техники вы планируете направить '
                                            f'{", ".join([el.__name__ for el in OfficeEquipment.__subclasses__()])}: ')
                        if user_answer == '-':
                            break
                        else:
                            if user_answer in [el.__name__ for el in OfficeEquipment.__subclasses__()]:
                                name_class = user_answer
                                working_class = [el for el in OfficeEquipment.__subclasses__() if el.__name__ == name_class][0]
                                while True:
                                    try:
                                        user_answer = input(f'Сколько единиц {name_class} вы хотите отправить: ')
                                        count = int(user_answer)
                                    except ValueError as err:
                                        print(f'Возникла ошибка({err}), введите число')
                                    else:
                                        break
                                while True:
                                    user_answer = input('Хотите задать подробные характеристики для каждой единицы? '
                                                        'Иначе будут заданы параметры по умолчанию. Введите + или - : ')
                                    if user_answer == '+':
                                        for x in range(1, count + 1):
                                            model, year, condition = (input(f'Для {name_class} {x} укажите через пробел '
                                                                            f'модель, год выпуска, новый или б.у. : ')).split()
                                            working_class(model, year, condition).be_kept(working_storage)
                                        break
                                    elif user_answer == '-':
                                        for i in range(count):
                                            working_class().be_kept(working_storage)
                                        break
                                print('Техника отправлена на склад. Продолжаем работу.')
                            else:
                                print('Такой вид техники недоступен')
                else:
                    print('Такого склада у нас нет')

    elif user_answer == 'перемещать технику между складами':
        print(f'-----------------------------\nДля возврата в главное меню введите -\nУ нашей компании есть склады: '
              f'{", ".join([i.name for i in Storage.list_storage])}.')
        while True:
            user_answer = input('Укажите, с какого склада нужно забрать технику: ')
            if user_answer == '-':
                break
            elif user_answer in [i.name for i in Storage.list_storage]:
                one_storage = [el for el in Storage.list_storage if el.name == user_answer][0]
                print(Storage.long_auditor(one_storage))
                while True:
                    try:
                        user_answer = input('Введите номера техники, которую хотите забрать, через пробел: ')
                        user_answer = [int(i) for i in user_answer.split()]
                        user_list = [el for ind, el in enumerate(one_storage.list_obj, 1) if ind in user_answer]
                        for i in user_list:
                            i.take_free(one_storage)
                        print('Вы забрали технику со склада')
                        while True:
                            user_answer = input('Укажите, на какой склад нужно отвезти технику: ')
                            if user_answer in [i.name for i in Storage.list_storage]:
                                two_storage = [el for el in Storage.list_storage if el.name == user_answer][0]
                                for i in user_list:
                                    i.be_kept(two_storage)
                                print(f'Техника доставлена на {two_storage.name}')
                                print(Storage.long_auditor(two_storage))
                                break
                            else:
                                print('Такого склада у нас нет')
                    except ValueError as err:
                        print(f'Возникла ошибка({err}), введите число')
                    else:
                        break
            else:
                print('Такого склада у нас нет')

    elif user_answer == 'отправиться на склад':
        while True:
            user_answer = input(f'-----------------------------\nДля возврата в главное меню введите -\n'
                                f'У нашей компании есть склады: {", ".join([i.name for i in Storage.list_storage])}.'
                                f'\nНа какой склад вы хотите отправиться? ')
            if user_answer == '-':
                break
            elif user_answer in [i.name for i in Storage.list_storage]:
                storage = [el for el in Storage.list_storage if el.name == user_answer][0]
                print(f'-----------------------------\nВы находитесь на складе {storage.name}'
                      f'\nЧтобы вернутьcя к выбору склада введите -')
                print(Storage.long_auditor(storage))
                while True:
                    user_answer = input('Введите номер техники, чтобы ей воспользоваться: ')
                    if user_answer == '-':
                        break
                    else:
                        try:
                            user_answer = int(user_answer)
                            use_technic = storage.list_obj[user_answer - 1]
                            print(f'Вы выбрали {use_technic.__class__.__name__}: Модель {use_technic.model}, '
                                  f'{use_technic.year} года выпуска\nНачинаем работу')
                            print(use_technic.use())
                        except ValueError as err:
                            print(f'Возникла ошибка({err}), введите число')
            else:
                print('Такого склада у нас нет')

    elif user_answer == 'завершить работу' or user_answer == 'Q':
        print('Работа программы окончена')
        break
