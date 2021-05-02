'''
 Урок 4. Задание 7.
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''
user_input = input("Введите целое число >>>")
if not user_input.isdigit():
    print("Неверный формат ввода")
    exit()
user_number = int(user_input)

factorial = 1


def fact(n):
    for number in range(1, (n + 1)):
        yield number


for user_item in fact(user_number):
    factorial *= user_item
    print(f"Факториал от {user_item} = {factorial}")