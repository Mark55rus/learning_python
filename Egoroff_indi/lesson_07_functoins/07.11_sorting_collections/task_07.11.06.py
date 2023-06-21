""" Напишите программу, которая отсортирует список subject_marks по убыванию оценок. Предметы, имеющие одинаковые
оценки, должны быть отсортированы в алфавитном порядке
    Затем распечатайте предметы и оценки, каждую пару на новой строке через пробел"""

subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
subject_marks.sort(key=lambda x: (-x[1], x[0]))
for elem in subject_marks:
    print(*elem)
