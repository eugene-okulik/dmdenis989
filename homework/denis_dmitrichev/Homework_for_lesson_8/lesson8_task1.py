# Задание:
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
import random


salary = int(input())
bonus = bool(random.randrange(0, 2))
if bonus:
    print(f'${salary + random.randrange(100, 1001)}')
else:
    print(f'${salary}')
