# Задание 3:
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из первого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение
def operation_selector(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first < second:
            operation = '/'
        elif first > second:
            operation = '-'
        else:
            operation = '+'
        return func(first, second, operation)
    return wrapper


@operation_selector
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    else:
        return first * second


print(calc(9, 0))
