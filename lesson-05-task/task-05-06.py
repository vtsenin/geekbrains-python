"""
 Урок 5. Задание 6.
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
user_dict = {}
value_sum_lab = 0
value_sum_lecture = 0
value_sum_practice = 0

with open('data_6.txt') as user_file:
    for line in user_file:
        key, *value = line.split()
        user_dict[key] = value
        for item in value:
            if item.find("(л)") > 0:
                value_sum_lecture = int(item[0:item.find("(л)")])
            if item.find("(пр)") > 0:
                value_sum_practice = int(item[0:item.find("(пр)")])
            if item.find("(лаб)") > 0:
                value_sum_lab = int(item[0:item.find("(лаб)")])

        user_dict[key] = value_sum_lab + value_sum_lecture + value_sum_practice
        value_sum_lab = 0
        value_sum_lecture = 0
        value_sum_practice = 0


    print(user_dict)
