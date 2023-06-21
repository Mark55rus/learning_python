""" Напишите программу, которая отсортирует список subject_marks по убыванию оценок.

Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел"""

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
for elem in sorted(subject_marks, key=lambda x: -x[1]):
    print(*elem)
