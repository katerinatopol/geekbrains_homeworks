'''
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

number = int(input("Введите целое положительное число: "))
max_numeral = 0

while number > 0:
    numeral = number % 10
    number = number // 10
    if numeral > max_numeral:
        max_numeral = numeral

print(f"Самая большая цифра в числе {max_numeral}")

