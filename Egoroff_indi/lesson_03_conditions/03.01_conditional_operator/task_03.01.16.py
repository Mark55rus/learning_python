""" Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.
    Программа должна выводить YES, когда клетки одного цвета, NO - разного. Гарантируется, что значение колонок это
латинские буквы abcdefgh, а строки это символы цифр от 1-8"""

# x, y = input(), input()
# color_x = ''
# color_y = ''
# if x[0] in 'aceg':
#     if int(x[1]) % 2 == 0:
#         color_x = 'white'
#     else:
#         color_x = 'black'
# else:
#     if int(x[1]) % 2 == 0:
#         color_x = 'black'
#     else:
#         color_x = 'white'
# if y[0] in 'aceg':
#     if int(y[1]) % 2 == 0:
#         color_y = 'white'
#     else:
#         color_y = 'black'
# else:
#     if int(y[1]) % 2 == 0:
#         color_y = 'black'
#     else:
#         color_y = 'white'
# if color_x == color_y:
#     print('YES')
# else:
#     print('NO')
a=input()
b=input()
abc = 'abcdefgh'
a1 = abc.index(a[0].lower())
b1 = abc.index(b[0].lower())
a2=int(a[1])
b2=int(b[1])
if (a1+a2)%2==(b1+b2)%2:
    print('YES')
else:
    print('NO')