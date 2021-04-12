"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from itertools import cycle
from time import sleep


class TrafficLight:

    def __init__(self, color=None):
        self.__color = color

    def running(self):
        color_list = [['red', 5], ['yellow', 2], ['green', 7]]
        if self.__color is not None:
            for el in color_list:
                if self.__color in el:
                    color_list = color_list[color_list.index(el):] + color_list[:color_list.index(el)]
                    break
        for color in cycle(color_list):
            yield color[0]
            sleep(color[1])


two_tl = TrafficLight(color='yellow') # Начинает работать с желтого сигнала
step = two_tl.running()
for j in range(5): # сколько раз сменить цвет
    print(next(step))
print()

first_tl = TrafficLight() # По умолчанию начинает работать с красного сигнала
step = first_tl.running()
for j in range(5): # сколько раз сменить цвет
    print(next(step))
print()

three_tl = TrafficLight(color='green') # Начинает работать с зеленого сигнала
step = three_tl.running()
for j in range(5): # сколько раз сменить цвет
    print(next(step))
print()
