"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def show_speed(self):
        return f"Машина {self.name} едет со скоростью {self.speed}"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, direction):
        return f"Машина {self.name} повернула {direction}"


class TownCar(Car):

    def show_speed(self):

        if self.speed > 60:
            return f"{super(TownCar, self).show_speed()} Превышение скорости!"
        else:
            return f"{super(TownCar, self).show_speed()} Все в порядке, продолжайте движение"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):

        if self.speed > 40:
            return f"{super(WorkCar, self).show_speed()} Превышение скорости!"
        else:
            return f"{super(WorkCar, self).show_speed()} Все в порядке, продолжайте движение"


class PoliceCar(Car):

    def true_police(self):
        if not self.is_police:
            return f"Машина {self.name} - не полицейская"
        else:
            return f"Машина {self.name} полицейская"


car_1 = TownCar(speed=40, color='grey', name='car_1', is_police=False)
print(car_1.go())
print(f"Цвет машины {car_1.name}: {car_1.color} ")
print(car_1.show_speed())
car_1.speed = 65
print(car_1.show_speed())
print(car_1.turn('направо'))
print(car_1.stop())
print()

car_2 = SportCar(speed=100, color='black', name='car_2', is_police=False)
print(car_2.go())
print(f"Цвет машины {car_2.name}: {car_2.color} ")
print(car_2.show_speed())
print(car_2.turn('налево'))
print(car_2.stop())
print()

car_3 = WorkCar(speed=30, color='black', name='car_3', is_police=False)
print(car_3.go())
print(f"Цвет машины {car_3.name}: {car_3.color} ")
print(car_3.show_speed())
car_3.speed = 50
print(car_3.show_speed())
print(car_3.turn('налево'))
print(car_3.stop())
print()

car_4 = PoliceCar(speed=100, color='black', name='car_3', is_police=True)
print(car_4.go())
print(f"Цвет машины {car_4.name}: {car_4.color} ")
print(car_4.show_speed())
print(car_4.turn('налево'))
print(car_4.stop())
print(car_4.true_police())