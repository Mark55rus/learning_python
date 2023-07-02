"""" Подвиг 10. Тестовый веб-сервер возвращает HTML-страницы по URL-адресам
(строкам). На вход программы поступают различные URL-адреса. Если адрес
пришел впервые, то на экране отобразить строку (без кавычек):
"HTML-страница для адреса <URL-адрес>"
Если адрес приходит повторно, то следует взять строку "HTML-страница для
адреса <URL-адрес>" из словаря и вывести на экран сообщение (без кавычек):
"Взято из кэша: HTML-страница для адреса <URL-адрес>"
Сообщения выводить каждое с новой строки.
P.S. Для считывания списка целиком в программе уже записаны начальные
строчки.
Input from task_06.01.11.txt"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for elem in lst_in:
    if elem not in d:
        d[elem] = elem
        print(f"HTML-страница для адреса {d[elem]}")
    else:
        print(f"Взято из кэша: HTML-страница для адреса {d[elem]}")
