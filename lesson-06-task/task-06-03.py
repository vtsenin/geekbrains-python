"""
 Урок 6. Задание 3.
Реализовать базовый класс Car (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут
должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Car.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.surname = surname
        self.name = name
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


john = Position("John", "Doe", "devops", {"wage": 100, "bonus": 10})
artur = Position("Artur", "Doe", "service", {"wage": 50, "bonus": 5})

print(john.get_full_name())
print(john.get_total_income())
print(artur.get_full_name())
print(artur.get_total_income())
