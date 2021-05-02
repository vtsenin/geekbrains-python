'''
 Урок 4. Задание 4.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
from collections import Counter

user_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

counter_duplicate = Counter(user_list)
nonduplicate_list = []

for key, value in counter_duplicate.items():
    if value < 2:
        nonduplicate_list.append(key)

res_list = [el for el in user_list if el in nonduplicate_list]
print(res_list)
