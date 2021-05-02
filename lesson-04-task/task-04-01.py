'''
 Урок 4. Задание 1.
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

import sys


def calculate(hours, rate_per_hour, bonus):
    """
    Функция расчета заработной платы сотрудника
    по формуле: (выработка в часах*ставка в час) + премия
    :param hours:
    :param rate_per_hour:
    :param bonus:
    :return:
    """
    try:
        return (hours * rate_per_hour) + bonus
    except:
        return  # return None


try:
    file, hours, rate_per_hour, bonus = sys.argv
except ValueError:
    print("Invalid args")
    exit()

try:
    print(calculate(int(hours), int(rate_per_hour), int(bonus)))
except ValueError:
    print("Invalid args")
    exit()