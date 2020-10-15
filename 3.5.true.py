"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def summator():
    total_sum = 0
    while True:
        num_list = input("Enter numbers: ")
        stopper = num_list.count("#")
        if stopper:
            total_sum += sum(map(int, num_list[:num_list.index("#") - 1].split()))
            break
        total_sum += sum(map(int, num_list.split()))
        print(f"Temporary sum value: {total_sum}")
    return total_sum


print(summator())