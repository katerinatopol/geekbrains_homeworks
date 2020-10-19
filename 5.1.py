"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("test.txt", "w") as f_obj:
    while True:
        content = input("Enter text: ")
        if not content:
            break
        f_obj.write(f"{content}\n")
