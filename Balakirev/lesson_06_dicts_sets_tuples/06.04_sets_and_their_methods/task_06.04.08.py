""" Подвиг 7. В аккаунте youtube Сергея прокомментировали очередное видео.
Некоторые посетители оставляли несколько комментариев. Требуется по списку
комментариев определить уникальное число комментаторов. Комментарии
поступают на вход программы в формате:
имя 1: комментарий 1
имя 2: комментарий 2
...
имя N: комментарий N
Также полагается, что имена у разных комментаторов не совпадают. Вывести на
экран общее число уникальных комментаторов.
P.S. Для считывания списка целиком в программе уже записаны начальные строчки.
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
commentators = set(name[0] for name in lst_in)
print(len(commentators))
