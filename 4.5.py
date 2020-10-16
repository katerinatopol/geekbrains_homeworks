"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from operator import mul
from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
# print(my_list)
result = reduce(mul, my_list)
print(result)
