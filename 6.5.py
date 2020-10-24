"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        super(Pen, self).draw()
        return "Рисует как ручка"


class Pencil(Stationery):
    def draw(self):
        super(Pencil, self).draw()
        return "Рисует как карандаш"


class Handle(Stationery):
    def draw(self):
        super(Handle, self).draw()
        return "Рисует как маркер"


pen_1 = Pen(title='pen_1')
print(pen_1.draw())
print()
pencil_1 = Pencil(title='pencil_1')
print(pencil_1.draw())
print()
handle_1 = Pen(title='handle_1')
print(handle_1.draw())