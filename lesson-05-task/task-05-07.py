"""
 Урок 5. Задание 7.
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

firm_dict = {}
firm_average_profit_dict = {}
number_profit = 0
average_profit = 0
profit_sum = 0
firm_list = []

with open('data_1.txt') as user_file:
    for line in user_file:
        key, *value = line.split()
        firm_dict[key] = int(value[1]) - int(value[2])
        profit = int(value[1]) - int(value[2])
        if profit > 0:
            profit_sum += profit
            number_profit += 1
    average_profit = profit_sum / number_profit

firm_list.append(firm_dict)
firm_average_profit_dict["average_profit"] = average_profit
firm_list.append(firm_average_profit_dict)

with open('firm.json', 'w') as file_stream:
    json.dump(firm_list, file_stream)

print(firm_list)
