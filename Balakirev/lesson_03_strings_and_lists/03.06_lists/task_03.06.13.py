""" Подвиг 12. Вводятся названия городов в одну строку через пробел. На основе
этой строки необходимо создать список lst и добавить его в конец следующего
списка:
    cities = ["Москва", "Тверь", "Вологда"]
Вывести результат на экран командой:
print(*lst)"""

cities = ["Москва", "Тверь", "Вологда"] + input().split()
print(*cities)
