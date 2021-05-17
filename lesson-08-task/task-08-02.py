"""
 Урок 8. Задание 2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyExceptionDivisionByZero(Exception):
    message = "Деление на ноль"

    def __str__(self):
        return self.message


class UserNumber(int):

    def __truediv__(self, other):
        if other is not None and not other:
            raise MyExceptionDivisionByZero

        return UserNumber(int(self) / int(other))


try:
    dividend, divider = map(UserNumber, input("Введите делимое и делитель через пробел: ").split())
    print(dividend / divider)
except MyExceptionDivisionByZero as e:
    print(e)
except ValueError as e:
    print(e)
