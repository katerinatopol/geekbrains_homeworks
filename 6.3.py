"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Full name worker: {self.name} {self.surname}"

    def get_total_income(self):
        return f"Total income: {sum(self._income.values())}"


manager = Position(name='Oleg', surname='Petrov', position='manager', wage=20000, bonus=5000)
print(manager.get_full_name())
print(manager.get_total_income())

teacher = Position(name='Tatyana', surname='Ivanova', position='teacher', wage=18000, bonus=8500)
print(teacher.get_full_name())
print(teacher.get_total_income())