"""
Урок 1. Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

# ввод времени  в секундах
user_input = input("Введите время в секундах >>>")

# проверка ввода
if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

# преобразуем секунды  в часы, минуты и секкунды
seconds_input = int(user_input)
print("Ввденое время:", seconds_input, "сек.")

hours = seconds_input // 3600
minutes = (seconds_input % 3600) // 60
seconds = seconds_input % 60

# кортежная запись
# hours, minutes, seconds = seconds_input // 3600, (seconds_input % 3600) // 60, seconds_input % 60

# выводим в формате чч:мм:сс
print("В формате чч:мм:сс это")
print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
