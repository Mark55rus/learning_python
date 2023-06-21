""" Бал в БерлГУ.
    По случаю 100500-летия Берляндского государственного университета совсем скоро состоится бал! Уже n юношей и m
девушек во всю репетируют вальс, менуэт, полонез и кадриль. Известно, что на бал будут приглашены несколько пар
юноша-девушка, причем уровень умений танцевать партнеров в каждой паре должен отличаться не более чем на единицу. Для
каждого юноши известен уровень его умения танцевать. Аналогично, для каждой девушки известен уровень ее умения
танцевать. Напишите программу, которая определит наибольшее количество пар, которое можно образовать из n юношей и m
девушек.
    Входные данные:
    В первой строке записано целое число n (1 ≤ n ≤ 100) — количество юношей. Вторая строка содержит последовательность
a1, a2, ..., an (1 ≤ ai ≤ 100), где ai — умение танцевать i-го юноши. Аналогично, третья строка содержит целое m
(1 ≤ m ≤ 100) – количество девушек. В четвертой строке содержится последовательность b1, b2, ..., bm (1 ≤ bj ≤ 100),
где bj — умение танцевать j-й девушки.
    Выходные данные:
    Выведите единственное число — искомое максимальное возможное количество пар.
    Примечание:
    В первом примере можно сочетать к примеру так 1-1, 4-5, 6-7 либо 2-1, 4-5, 6-7. В любом случае можно составить
только три пары"""

n = int(input())
lst_boys = list(map(int, input().split()))
lst_boys.sort()
m = int(input())
lst_girls = list(map(int, input().split()))
lst_girls.sort()
count = 0
boys = 0
girls = 0
while boys < n and girls < m:
    if abs(lst_boys[boys] - lst_girls[girls]) <= 1:
        count += 1
        boys += 1
        girls += 1
    elif lst_boys[boys] < lst_girls[girls]:
        boys += 1
    else:
        girls += 1
print(count)
