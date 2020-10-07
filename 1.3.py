'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

# Вариант 1
number = input("Введите число меньше 10: ")

number_1 = int(number)
number_2 = int(number * 2)
number_3 = int(number * 3)
result = number_1 + number_2 + number_3
print(result)

# Вариант 2
variable = int(input("Введите число меньше 10: "))

variable_2 = variable * 11
variable_3 = variable * 111
result_2 = variable + variable_2 + variable_3
print(result_2)
