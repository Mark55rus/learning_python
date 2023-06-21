""" В этой задаче вам необходимо скачать файл, в котором записаны натуральные числа. Ваша задача найти
- количество трехзначных чисел;
- сумму двухзначных чисел
    В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов. Сперва количество,
потом сумма"""


# variant 1:
def reading_file(name: str) -> None:
    count_three_digits = 0
    total_two_digits = 0
    file = open(name, encoding='utf-8')
    for i in file:
        if len(i.strip()) == 2:
            total_two_digits += int(i.strip())
        if len(i.strip()) == 3:
            count_three_digits += 1
    file.close()
    print(count_three_digits, total_two_digits, sep=',')


reading_file("task_09.01.09.txt")

# variant 2:
sm, sk = 0, 0

for n in map(int, open('task_09.01.09.txt')):
    if 9 < n < 100:
        sm += n
    elif 99 < n < 1000:
        sk += 1

print(f'{sk},{sm}')
