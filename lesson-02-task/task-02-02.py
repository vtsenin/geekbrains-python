'''
 Урок 2. Задание 2.
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

list_data = []
list_index = 1


# number of elements
number = int(input("Enter number of elements : "))

# fil list
for i in range(0, number):
    list_element = int(input())
    list_data.append(list_element)

print(list_data)

while list_index < len(list_data):
    list_data[list_index - 1], list_data[list_index] = list_data[list_index], list_data[list_index - 1]
    list_index += 2

print(list_data)


