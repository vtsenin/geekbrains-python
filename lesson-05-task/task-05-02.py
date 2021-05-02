"""
 Урок 5. Задание 2.
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

lines = 0
words = 0
with open('data_2.txt') as user_file:
    for line in user_file:
        words = len(line.split())
        print(f"Количество слов в {lines + 1} строке = {words}")
        lines += 1

print(f"Количество строк в файле = {lines}")
