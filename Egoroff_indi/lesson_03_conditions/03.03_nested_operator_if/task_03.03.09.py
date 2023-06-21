""" При игре в "Города" игроки по очереди называют названия городов так, чтобы первая буква каждого нового слова
совпадала с последней буквой предыдущего. При этом считают, что если последняя буква предыдущего слова — мягкий знак,
то с первой буквой следующего слова надо сравнивать букву, предшествующую мягкому знаку.
    Напишите программу, которая считывает подряд две строки, после чего выводит «Good», если последний символ первой
строки совпадает с первым символом второй (с учётом правила про мягкий знак), и «Bad» в противном случае."""

city1, city2 = input().lower(), input().lower()
if city1[-1] == 'ь':
    if city1[-2] == city2[0]:
        print('Good')
    else:
        print('Bad')
else:
    if city1[-1] == city2[0]:
        print('Good')
    else:
        print('Bad')
