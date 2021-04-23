'''
 Урок 3. Задание 1.
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def division_func(var_1, var_2):
    """
    Функция, принимающая два числа (позиционные аргументы) и выполняющую их деление
    :param var_1: Первое число
    :param var_2: Второе число
    :return:
    """
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return f"Деление на ноль!!!"

def user_input():
    """
    Запрос числа у пользователя
    :return:
    :rtype int
    """
    user_input = input(f"Введите число >>>")
    if not user_input.isdigit():
        print("Неверный формат ввода")
        exit()
    return int(user_input)

num_1 = user_input()
num_2 = user_input()

print(division_func(num_1, num_2))
