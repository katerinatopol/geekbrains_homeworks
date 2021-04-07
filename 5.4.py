"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []

with open("for5.4.txt", "r") as file:
    for line in file:
        line = line.split(" - ")
        new_file.append(translate.get(line[0]) + " - " + line[1])
    print(" \n".join(new_file))

with open("new_file.txt", "w") as file:
    file.writelines(new_file)
