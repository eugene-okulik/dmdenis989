# Задание 2:
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
import sys


def fibonacci_sequence():
    fib1 = 0
    fib2 = 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


sys.set_int_max_str_digits(100000)
counter = 1
for number in fibonacci_sequence():
    if counter in [5, 200, 1000]:
        print(f"Позиция {counter}: {number}")
    elif counter == 100000:
        print(f"Позиция {counter}: {number}")
        break
    counter += 1
