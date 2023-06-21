n = int(input())
i = 1
count = 0
while i * i <= n:
    if n % i == 0:
        count += i
        if i != n // i:
            count += n // i
    i += 1
print(count)

