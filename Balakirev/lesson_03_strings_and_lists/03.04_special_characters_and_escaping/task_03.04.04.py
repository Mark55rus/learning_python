""" Подвиг 3. Вводится два слова в одну строку через пробел. Поставьте между
этими словами символ обратного слеша (вместо пробела). Результирующую строку
отобразите на экране.
    P.S. Задачу реализовать без применения F-строк."""

text = input()
print(text.replace(' ', '\\'))
