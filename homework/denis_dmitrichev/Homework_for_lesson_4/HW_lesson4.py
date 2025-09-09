my_dict = {'tuple': (3, 5, 3, 6, 8), 'list': ['one', 2, {2: 4}, (1, 2), [1, 2]],
           'dict': {'a': 3, 'b': 4, 'c': 5, 'g': 30, 'h': 40}, 'set': {1, 7, 4, 'name', 5}}
# Вывести последний элемент в значении ключа tuple:
print(my_dict['tuple'][-1])
# Значению под ключом list добавить в конец еще один элемент; удалить второй элемент списка:
my_dict['list'].append("New_element")
my_dict['list'].pop(1)
# Добавить элемент с ключом ('i am a tuple',) и любым значением; удалить любой элемент:
my_dict['dict'][("i am a tuple",)] = '40'
my_dict['dict'].pop('a')
# Добавить новый элемент в множество, удалить элемент из множества
my_dict['set'].add(40)
my_dict['set'].pop()
print(my_dict)
