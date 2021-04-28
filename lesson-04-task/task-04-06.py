'''
 Урок 4. Задание 6.
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
'''
from itertools import count
from itertools import cycle
import time

user_input = input("Введите целое число >>>")
if not user_input.isdigit():
    print("Неверный формат ввода")
    exit()
user_number = int(user_input)


for x in count(user_number, 1):
    if x > 10:
        break

    print(x)

print("Done count")

cycle_list = [1, 2, 5]
cycle_count = 1
for x in cycle(cycle_list):
    if cycle_count > 5:
        break
    print(x)
    cycle_count += 1

print("Done cycle")
