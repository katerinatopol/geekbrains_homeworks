"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
sum_user_answer = 0
game = True

while game:
    user_answer = input("Game over: enter 'q'. \nEnter numbers separated by a space: ").split()
    for i in user_answer:
        try:
            sum_user_answer += int(i)
        except ValueError as err:
            if i == 'q':
                game = False
            else:
                print(f"{err}\nIt's not number: {i}, try again")
            break
    print(sum_user_answer)

print(f"Game over")