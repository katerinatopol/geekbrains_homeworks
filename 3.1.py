"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""


def division(*args):
    try:
        one_number, two_number = [int(i) for i in input("Enter two numbers separated by a space: ").split()]
        result = one_number / two_number
        return f"Division result: {result}"
    except ValueError as err:
        return f"An error occurred: {err}"
    except ZeroDivisionError as err:
        return f"An error occurred: {err}"


print(division())
