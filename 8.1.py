"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def to_int(cls, string):
        day, month, year = map(int, string.split('-'))
        return day, month, year

    @staticmethod
    def validation(date):
        day, month, year = Date.to_int(date)
        if year > 0:                                       # год положительное число
            if month != 2:        # все месяцы кроме февраля
                if month in list([1, 3, 5, 7, 8, 10, 12]): # месяцы где 31 день
                    if day not in range(1, 32):
                        raise ValueError('Day not valid')
                elif month in list([4, 6, 9, 11]):          # месяцы где 30 дней
                    if day not in range(1, 31):
                        raise ValueError('Day not valid')
                else:
                    raise ValueError('Month not valid')
            elif month == 2:                                              # февраль
                if Date.leap_year(year):  # проверка на високосный год
                    if day not in range(1, 29):
                        raise ValueError('Day not valid')
                else:
                    if day not in range(1, 30):
                        raise ValueError('Day not valid')
        else:
            raise ValueError('Year not valid')
        return 'Data valid'

    @staticmethod
    def leap_year(year):
        if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True



one_obj = Date('29-2-2020')
print(one_obj.validation('29-2-2020'))

# two_obj = Date('29-2-2019')
# print(two_obj.validation('29-2-2019'))
#
# three_obj = Date('29-2-1944')
# print(three_obj.validation('29-2-1944'))
#
# four_obj = Date('29-14-2020')
# print(four_obj.validation('29-14-2020'))
#
# five_obj = Date('34-8-2020')
# print(five_obj.validation('34-8-2020'))
