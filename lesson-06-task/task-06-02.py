"""
 Урок 6. Задание 2.
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length: int  # длина дороги в метрах
    _width: int  # ширина дороги в метрах
    _weight: float  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
    _height: int  # толщина покрытия

    def __init__(self, length: int, width: int, weight=0.025, height=5):
        self._length = length
        self._width = width
        self._weight = weight
        self._height = height

    def get_road_weight(self):
        try:
            return (self._length * self._width * self._weight * self._height)
        except TypeError:
            return None


road = Road(5000, 20)
print(f"массы асфальта = {road.get_road_weight()} тонн")
