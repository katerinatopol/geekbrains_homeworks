"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
from math import ceil


class Clothes(ABC):
    @abstractmethod
    def consumption_cloth(self):
        pass

    @staticmethod
    def sum_consumption(*args):
        return sum(el.consumption_cloth for el in args)


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption_cloth(self):
        return ceil(self.size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption_cloth(self):
        return ceil(2 * self.height + 0.3)


coat_1 = Coat(42)
print(f"Consumption cloth for coat: {coat_1.consumption_cloth}m")
suit_1 = Suit(1.8)
print(f"Consumption cloth for suit: {suit_1.consumption_cloth}m")

coat_2 = Coat(40)
suit_2 = Suit(1.7)
coat_4 = Coat(48)

print(f"Consumption cloth: {Clothes.sum_consumption(coat_1, coat_2, suit_2, coat_4)}m")
