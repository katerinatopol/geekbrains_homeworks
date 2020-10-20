"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import csv

# Вариант с генератором
with open("for5.3.csv", "r") as file:
    reader = csv.reader(file)
    last_name = [row[0] for row in reader if int(row[1]) < 20000]
    print(f"Employees with a salary of less than 20000 rub.: \n" + "  \n".join(last_name))
    file.seek(0)
    count_lines = len(file.readlines())
    file.seek(0)
    total = (sum(int(row[1]) for row in csv.reader(file)))
    print(f"Average salary: {total / count_lines} rub.")

# Вариант с циклом
with open("for5.3.csv", "r") as file:
    reader = csv.reader(file)
    print("Employees with a salary of less than 20000 rub.: ")
    count_lines = 0
    total = 0
    for row in reader:
        if int(row[1]) < 20000:
            print(f"{row[0]} ({row[1]} rub.)")
        count_lines += 1
        total += int(row[1])
    print(f"Average salary: {total / count_lines} rub.")
