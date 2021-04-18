"""
Урок 1. Задание 3.
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
# ввод числа
user_input = input("Введите число n >>>")

# проверка ввода
if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

# пример через дмапазон
result = 0
for x in range(1, 4):
    result += int(user_input * x)
print("Сумма чисел n + nn + nnn:", result)

"""
# пример подсчета через while
user_number = int(user_input)
characters_count = 0
temp_number = user_number

while temp_number:
    temp_number //= 10
    characters_count += 1

first_level_multiplication = (10 * characters_count) + 1
second_level_multiplication = (10 ** (characters_count * 2)) + first_level_multiplication

result = user_number + (user_number * first_level_multiplication) + (user_number * second_level_multiplication)

print("Сумма чисел n + nn + nnn:", result)
"""

"""
# перевод чила в тип int
number = int(user_input)

# считаем  сумму чисел n + nn + nnn
sum = number + (number * 10 + number) + (number * 100 + number * 10 + number)
temp = 23 + 2323 + 232323
# выыодим ответ
print("Сумма чисел n + nn + nnn:", sum)
"""
