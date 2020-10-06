'''
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
'''

variable_one = 10
variable_two = 34
variable_three = 'строка'
variable_four = False

print(variable_one, variable_two, variable_three, variable_four)

number_one = int(input("Введите число: "))
number_two = int(input("Введите еще одно число: "))
name = input("Как вас зовут? ")
surname = input("А фамилия? ")

# print(number_one, number_two, name, surname)
print(f"Привет, {name} {surname}. Вы ввели числа {number_one} и {number_two}")