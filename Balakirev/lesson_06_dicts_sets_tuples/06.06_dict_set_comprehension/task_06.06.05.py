""" Подвиг 4. Вводится текст в одну строчку со словами через пробел. С
помощью генератора множеств сформировать множество из уникальных слов без
учета регистра и длина которых не менее трех символов. Вывести на экран
размер этого множества."""

my_set = {word.lower() for word in input().split() if len(word) >= 3}
print(len(my_set))
