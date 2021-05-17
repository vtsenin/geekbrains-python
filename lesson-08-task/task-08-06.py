"""
 Урок 8. Задание 5.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class TransferStorageError(Exception):
    def __init__(self, text):
        self.text = f"Error:\n {text}"

    def __str__(self):
        return self.text


class Warehouse:
    def __init__(self):
        self.__warehouse = []

    def add(self, item: "OfficeEquipment"):
        self.__warehouse.append(item)

    def transfer(self, idx , department: str):
        if isinstance(idx, int):
            item: OfficeEquipment = self.__warehouse[idx]
            item.department = department
        else:
            raise TransferStorageError(f"Введен неправильный тип данных для перемещения по департаментам")


    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__warehouse[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__warehouse[key]

    def __iter__(self):
        return self.__warehouse.__iter__()

    def __str__(self):
        return f"На складе всего {len(self.__warehouse)} устройств"


class OfficeEquipment:
    input_voltage = 220
    network_card = True

    def __init__(self, type: str, vendor: str, model: str, color: str, price: float):
        self.type = type
        self.vendor = vendor
        self.model = model
        self.color = color
        self.price = price
        self.department = None

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} {self.color} ({self.department})"

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)


class Printer(OfficeEquipment):

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):

    def __init__(self, *args):
        super().__init__('Сканнер', *args)


class Xerox(OfficeEquipment):

    def __init__(self, *args):
        super().__init__('Ксерокс', *args)


ware_house = Warehouse()
ware_house.add(Printer("HP", "8500", "white", 3000))
ware_house.add(Scanner("Epson", "Scan1200", "white", 20000))
ware_house.add(Xerox("Xerox", "3000", "white", 100000))

print(ware_house)

try:
    ware_house.transfer('123', 'департамент 1')
except TransferStorageError as e:
    print(e)


print(ware_house[0])
ware_house.transfer(0, 'департамент 3')
print(ware_house[0])
