from string import ascii_lowercase, ascii_uppercase
from random import randint, seed

chars = ascii_lowercase + ascii_uppercase
seed(1)


def generate_mail(num):
    while True:
        mail = ''
        for _ in range(num):
            indx = randint(0, len(chars) - 1)
            mail += chars[indx]
        mail += "@mail.ru"
        yield mail


n = int(input())
new_mail = generate_mail(n)
for _ in range(5):
    print(next(new_mail))
