# Задание 1 - Угадайка
my_number = 4
message = "Угадай число: "
while True:
    user_number = int(input(message))
    if my_number == user_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        message = "Неверно! Попробуйте снова: "

# my_number = 5
# user_number = int(input("Угадай загаданное число!: "))
# while my_number != user_number:
#     user_number = int(input("Неверно! Попробуйте снова: "))
# print("Поздравляю! Вы угадали!")
