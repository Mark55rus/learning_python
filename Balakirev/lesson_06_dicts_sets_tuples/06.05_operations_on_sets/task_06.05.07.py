""" Подвиг 6. Вводятся два списка городов каждый с новой строки (в строке
названия через пробел), которые объехал Сергей в 1-й и 2-й годы своего
путешествия по России. Требуется определить, включал ли его маршрут во 2-й
год все города 1-го года путешествия? Если это так, то вывести ДА, иначе -
НЕТ."""

set1, set2 = [set(input().split()) for _ in range(2)]
if set1.issubset(set2):
    print("ДА")
else:
    print("НЕТ")

# variant 2:
# print('ДА' if set1 <= set2 else 'НЕТ')
