"""Выиграть в лотерею.
    У Олега в банке есть n евро. Он хочет снять всю сумму наличными. Номиналы евро купюр равны 1, 5, 10, 20, 100. Какое
минимальное число купюр должен получить Олег после того, как снимет все деньги? На вход программе поступает одно
положительные целое число n."""

n = int(input())
count = 0
count += n // 100
count += n % 100 // 20
count += n % 20 // 10
count += n % 10 // 5
count += n % 5 // 1
print(count)