"""
 Урок 5. Задание 3.
Создать текстовый файл (не программно), построчно записать фамилии сотрудникови величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:

Иванов 23543.12
Петров 13749.32
"""

person = 1
salary_sum = 0
with open('data_3.txt') as user_file:
    for line in user_file:
        words = line.split()
        try:
            if int(words[1]) < 20000:
                print(words[0])
        except IndexError:
            print("Ошибка в файле")

        person += 1
        salary_sum +=int(words[1])

print(f"Средняя величина дохода сотрудников = {salary_sum/person}")




