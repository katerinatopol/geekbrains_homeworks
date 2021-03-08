'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
seasons_list = [
    "winter",
    "winter",
    "spring",
    "spring",
    "spring",
    "summer",
    "summer",
    "summer",
    "autumn",
    "autumn",
    "autumn",
    "winter"
]
seasons_dict = {
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
        month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
        print(f"{month} месяц относится к времени года (согласно list): {seasons_list[month - 1]}")
        print(f"{month} месяц относится к времени года (согласно dict): {seasons_dict[month]}")
        break
    except ValueError as err:
        print("Это не число, попробуйте еше раз", err)
    except KeyError as err:
        print(f"Такого месяца {err} не существует, попробуйте еще раз")
    except IndexError as err:
        print("Такого месяца не существует, попробуйте еще раз", err)

# except KeyError или IndexError возникает в зависимости от того, какая строка в print стоит первой. Какое исключение возникло первым, то и обработалось.
