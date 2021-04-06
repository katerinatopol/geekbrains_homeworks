"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        znak = ''
        if self.im > 0:
            znak = '+'
        return f'{self.re}{znak}{self.im}*j'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


one_number = ComplexNumber(3, 4)
two_number = ComplexNumber(2, -7)
print(one_number)
print(two_number)
print(f'{one_number} + {two_number} = {one_number + two_number}')
print(f'{one_number} * {two_number} = {one_number * two_number}')
