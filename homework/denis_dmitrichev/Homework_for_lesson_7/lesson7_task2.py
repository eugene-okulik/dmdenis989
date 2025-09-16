# Задание 2:
# Выведите на экран каждый ключ столько раз сколько указано в значении.
def print_simbols(dict1):
    for key, value in dict1.items():
        print(key * value)


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
print_simbols(words)
