'''
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
# Если нам без разницы что введет пользователь:
# my_list = input("Введите несколько чисел или слов через пробел: ").split(" ")

# Если хотим чтобы пользователь вводил строго числа:
while True:
    try:
        my_list = [int(i) for i in input("Введите несколько чисел через пробел: ").split()]
    except ValueError:
        print("Это не числа, попробуйте еше раз")
    else:
        break

print(f"Вы создали список {my_list}")

for i in range(len(my_list))[::2]:
    if i == len(my_list) - 1:
        break
    else:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]


print(f"Теперь он выглядит так {my_list}")

# улучшение варианта с range:
for i in range(1, len(my_list), 2):
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]


print(f"Поворот {my_list}")

# Вариант с while (range лучше по памяти)
i = 0
while i + 1 < len(my_list):
    if i % 2 == 0:
        elem = my_list.pop(i + 1)
        my_list.insert(i, elem)
    i += 1
print(f"И в обратную сторону {my_list}")