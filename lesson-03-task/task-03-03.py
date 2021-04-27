'''
 Урок 3. Задание 3.
 Реализовать функцию my_func(),
 которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
'''


def my_func(arg_1, arg_2, arg_3):
    return arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)

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
num_3 = user_input()

print(my_func(num_1, num_2, num_3))
