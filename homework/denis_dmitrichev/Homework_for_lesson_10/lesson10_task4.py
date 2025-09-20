# Задание 4:
# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


new_list = [cut_string[:-1].split() for cut_string in PRICE_LIST.split('\n')]
new_dict = {key: int(value) for key, value in new_list}
print(new_dict)
