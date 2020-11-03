"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


one_numbers, two_numbers = (input('Enter two numbers separated by space: ')).split()

try:
    one_numbers, two_numbers = int(one_numbers), int(two_numbers)
    if two_numbers == 0:
        raise OwnError('Error: division by zero!')
    result = one_numbers / two_numbers

except ValueError as err:
    print(f'Error: {err}')

except OwnError as err:
    print(err)

else:
    print(f'Result: {result}')
