""" Сколько дней в месяце?
    Программа получает на вход номер месяца - натуральное число N (1 ≤ N ≤ 12) и в зависимости от его значения выводит
количество дней в месяце. Будем считать, что год невисокосный. При решении конечно же используйте оператор match-case
Январь - 31 день
Февраль - 28 дней
Март - 31 день
Апрель - 30 дней
Май - 31 день
Июнь - 30 дней
Июль - 31 день
Август - 31 день
Сентябрь - 30 дней
Октябрь - 31 день
Ноябрь - 30 дней
Декабрь - 31 день"""

n = int(input())
match n:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(31)
    case 4 | 6 | 9 | 11:
        print(30)
    case 2:
        print(28)
