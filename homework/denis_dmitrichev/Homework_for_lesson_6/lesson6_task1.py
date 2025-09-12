# Задание 1:
# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero” и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова. Если после слова идет запятая или точка,
# этот знак препинания должен идти после того же слова, но уже преобразованного.
new_string = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
              'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = new_string.split()
new_words = []
for word in words:
    if word.endswith(',') or word.endswith('.'):
        new_words.append(word[:-1] + 'ing' + word[-1])
    else:
        new_words.append(word + 'ing')
new_string2 = ' '.join(new_words)
print(new_string2)
