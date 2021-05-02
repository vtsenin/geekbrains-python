"""
 Урок 5. Задание 1.
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('data_6.txt', 'w') as user_file:
    while True:
        try:
            if user_file.writable():
                user_input = input(
                    "Введите потсрочные данные. (Об окончании ввода данных свидетельствует пустая строка) >>>") + "\n"
                if user_input == "\n":
                    raise KeyboardInterrupt
                else:
                    user_file.writelines(user_input)
            else:
                print("Cant write")
        except KeyboardInterrupt:
            break
