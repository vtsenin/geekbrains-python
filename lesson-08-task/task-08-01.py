"""
 Урок 8. Задание 1.
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:

    @staticmethod
    def data_validate(content: str):
        data_string = content.split('-')

        if int(data_string[0]) < 0 or int(data_string[0]) > 31:
            raise ValueError(f"{data_string[0]} неверный формат даты(«день-месяц-год»)")

        if int(data_string[1]) < 0 or int(data_string[1]) > 12:
            raise ValueError(f"{data_string[1]} неверный формат даты(«день-месяц-год»)")

        return data_string

    @classmethod
    def data_normalize(cls, content: str):
        a = cls.data_validate(content)
        normalize = []
        for x in a:
            normalize.append(int(x))
        return normalize


temp_string = "01-03-1986"

print(Data.data_validate(temp_string))
print(Data.data_normalize(temp_string))
