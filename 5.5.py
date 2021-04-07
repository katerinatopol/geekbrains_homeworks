"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("for5.5.txt", "w") as file:
    line = input("Enter numbers separated space: ")
    file.writelines(line)
    numbers = [int(i) for i in line.split()]
    print(f"Sum of numbers: {sum(numbers)}")
