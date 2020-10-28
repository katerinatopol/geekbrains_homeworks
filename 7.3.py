"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class OrganicCage:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        new_cage_quantity = self.quantity + other.quantity
        self.quantity = None
        other.quantity = None
        print(f"Клетки объединились в новую клетку, количество ячеек: {new_cage_quantity}")
        return OrganicCage(new_cage_quantity)

    def __sub__(self, other):
        return f"результат вычитания клеток: {self.quantity - other.quantity}" if (self.quantity - other.quantity) > 0 else 'Error'

    def __mul__(self, other):
        new_cage_quantity = self.quantity * other.quantity
        self.quantity = None
        other.quantity = None
        print(f"Клетки объединились в новую клетку, количество ячеек: {new_cage_quantity}")
        return OrganicCage(new_cage_quantity)

    def __truediv__(self, other):
        new_cage_quantity = round(self.quantity // other.quantity)
        self.quantity = None
        other.quantity = None
        print(f"Клетки объединились в новую клетку, количество ячеек: {new_cage_quantity}")
        return OrganicCage(new_cage_quantity)

    def make_order(self, row):
        return (self.quantity // row) * (row * '*' + '\n') + (self.quantity % row) * '*'


cage_1 = OrganicCage(11)
cage_2 = OrganicCage(8)
cage_3 = OrganicCage(13)
cage_4 = OrganicCage(21)
cage_5 = OrganicCage(2)

print(cage_1.make_order(5))

cage_6 = cage_1 + cage_2
print(cage_6.quantity) # новая клетка
print(cage_1.quantity) # уже пустая

print(cage_6 - cage_3)
print(cage_6 - cage_4)

cage_7 = cage_3 * cage_4
cage_8 = cage_7 / cage_5
