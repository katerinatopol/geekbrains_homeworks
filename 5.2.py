"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("for5.2.txt", "r") as f_obj:
    count_lines = len(f_obj.readlines())
    print(f"The document has {count_lines} lines")
    f_obj.seek(0)
    line_number = 0
    for line in f_obj:
        line_number += 1
        count_words = len(line.split())
        print(f"Line number {line_number} consists of {count_words} words.")
