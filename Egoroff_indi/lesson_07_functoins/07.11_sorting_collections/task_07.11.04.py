""" Напишите программу, которая отсортирует список subject_marks по возрастанию оценок. Затем распечатайте предметы и
оценки, каждую пару на новой строке через пробел"""

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
subject_marks.sort(key=lambda x: x[1])
for elem in subject_marks:
    print(*elem)
