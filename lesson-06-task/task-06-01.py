"""
 Урок 6. Задание 1.
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    __color: str
    __traffic_status: dict = {"красный": 7, "желтый": 2, "зеленый": 5}
    __start_flag: bool = False

    def __init__(self, color: str):
        self.__color = color

    def running(self):
        for color, color_time in self.__traffic_status.items():
            if self.__color == color:
                print(f"Светофор в режиме '{self.__color}' на {color_time} секунд")
                time.sleep(color_time)
                self.__start_flag = True
            elif self.__start_flag:
                self.__color = color
                print(f"Светофор в режиме '{self.__color}' на {color_time} секунд")
                time.sleep(color_time)


traffic_light = TrafficLight("желтый")
traffic_light.running()
