"""
 Урок 5. Задание 5.
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('data_5.txt', 'w') as user_file:
    while True:
        try:
            if user_file.writable():
                user_input = input(
                    "Введите набор чисел, разделенных пробелами. (Об окончании ввода данных свидетельствует пустая строка) >>>") + "\n"
                if user_input == "\n":
                    raise KeyboardInterrupt
                else:
                    user_file.writelines(user_input)
            else:
                print("Cant write")
        except KeyboardInterrupt:
            break

with open('data_5.txt') as user_file:
    numbers_sum = 0
    for line in user_file:
        numbers = line.split()
        for number in numbers:
            if number.isdigit():
                numbers_sum += int(number)

    print(f"Сумма чисел в файле = {numbers_sum}")
