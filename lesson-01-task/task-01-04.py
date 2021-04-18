"""
Урок 1. Задание 4.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

# ввод целого положительного числв
user_input = input("Введите целое положительное число >>>")

# проверка ввода
if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

number = int(user_input)
number_max = 0

# поиск самой большой цифры  в числе
while number and number_max != 9:
    if number_max < (number % 10):
        number_max = number % 10
    number = number // 10

# выводим ответ
print("Самая большая цифра в числе", number_max)



