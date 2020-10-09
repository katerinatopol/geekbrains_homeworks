'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
# Решение через list
seasons_ls = [
    ["зима", 12, 1, 2],
    ["весна", 3, 4, 5],
    ["лето", 6, 7, 8],
    ["осень", 9, 10, 11]
]
while True:
    try:
        user_answer = int(input("Введите месяц в виде целого числа от 1 до 12: "))
        if user_answer > 12 or user_answer < 1:
            print("Такого месяца не существует, попробуйте еще раз")
            continue
    except ValueError:
        print("Это не число, попробуйте еше раз")
    else:
        break

for i in range(len(seasons_ls)):
    if user_answer in seasons_ls[i]:
        print(f"{user_answer} месяц относится к времени года: {seasons_ls[i][0]}")
        break


# Решение через dict
seasons = {
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень",
    12: "зима",
}
while True:
    try:
        user_answer = int(input("Введите месяц в виде целого числа от 1 до 12: "))
    except ValueError:
        print("Это не число, попробуйте еше раз")
    else:
        try:
            # ???? почему не работает такая запись: seasons.get(user_answer) выводит None не смотря на except. Он не считает KeyError если есть None?
            print(f"{user_answer} месяц относится к времени года: {seasons[user_answer]}")
            break
        except KeyError:
            print("Такого месяца не существует, попробуйте еще раз")


