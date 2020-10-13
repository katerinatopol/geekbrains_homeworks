"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def information(name, last_name, year, city, email, telephone):
    return ", ".join([name, last_name, year, city, email, telephone])


print(f"Info about user: {information(name='Kate', last_name='Topol', year='1995', city='SPb', email='@mail.ru', telephone='8-900')}")