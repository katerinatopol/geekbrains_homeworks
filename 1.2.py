'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''
user_answer = int(input("Введите время в секундах: "))
seconds = user_answer % 60
minutes = (user_answer // 60) % 60
hours = (user_answer // 60) // 60
result = '%02d:%02d:%02d' % (hours, minutes, seconds)
print(f"{user_answer} секунд равно: {result}")
