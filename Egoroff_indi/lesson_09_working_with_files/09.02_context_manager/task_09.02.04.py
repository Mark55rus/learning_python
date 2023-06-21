""" В вашем распоряжении имеется следующий файл. Ваша задача скачать его и найти сколько уникальных слов используется в
этом тексте, при этом регистр букв не нужно учитывать. Это значит, что слова Lorem и loRem являются эквивалентными.
    Например, если перед вами был бы такой текст:
- Привет как дела
- привет хорошо
то здесь четыре уникальных слова.
    Между словами в файле стоят только пробелы и переносы строк, других разделителей нет.
В качестве ответа укажите количество уникальных слов """

# variant 1:
my_set = set()
with open('task_09.02.04.txt', 'r', encoding='utf-8') as file:
    for row in file:
        for word in row.split():
            my_set.add(word.lower())
    file.close()
print(len(my_set))

# variant 2:
with open('task_09.02.04.txt', encoding='utf-8') as file:
    print(len(set(file.read().lower().split())))
