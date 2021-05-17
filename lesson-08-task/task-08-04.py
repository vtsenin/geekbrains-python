"""
 Урок 8. Задание 4.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    pass


class OfficeEquipment:
    input_voltage = 220
    network_card = True

    def __init__(self, type: str, vendor: str, model: str, color: str, price: float):
        self.type = type
        self.vendor = vendor
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):

    def __init__(self, *args):
        super().__init__('Сканнер', *args)


class Xerox(OfficeEquipment):

    def __init__(self, *args):
        super().__init__('Ксерокс', *args)


p1 = Printer("Epson", "XP-400", "white", 4000)
print(p1)
