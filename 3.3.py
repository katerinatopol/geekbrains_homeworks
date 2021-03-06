"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    my_list.remove(min(var_1, var_2, var_3))
    return sum(my_list)


print(my_func(100, 7, 200))
