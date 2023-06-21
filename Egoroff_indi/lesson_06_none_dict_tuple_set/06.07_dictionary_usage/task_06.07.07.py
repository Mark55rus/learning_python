dct = {}
s = 'aaasdsadqweqwesfdaffqwer'
for c in s:
    dct[c] = dct.get(c, 0) + 1
print(dct)