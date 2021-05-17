"""
 Урок 7. Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).

Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    _clothes_name: str

    @abstractmethod
    def calculate_tissue_consumption(self):
        pass


class Coat(AbstractClothes):
    def __init__(self, v: float):
        self.v = v

    @property
    def calculate_tissue_consumption(self):
        return float('{:.2f}'.format(self.v / 6.5 + 0.5))


class Suit(AbstractClothes):
    def __init__(self, h: float):
        self.h = h

    @property
    def calculate_tissue_consumption(self):
        return float('{:.2f}'.format(2 * self.h + 0.3))

coat_test = Coat(48)
print(f"Расхода ткани для пальто (V/6.5 + 0.5) = {coat_test.calculate_tissue_consumption}")
suit_test = Suit(1.8)
print(f"Расхода ткани для костюма (2*H + 0.3) = {suit_test.calculate_tissue_consumption}")

