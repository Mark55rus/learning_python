"""Правильная скобочная последовательность 🌶️.
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из
    символов "(" и ")" и возвращает значение True, если поступившая на вход строка является правильной скобочной
    последовательностью и False в противном случае.
Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов "(" и ")" где
    каждой открывающей скобке найдется парная закрывающая скобка.
Примечание 2. Следующий программный код:
print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
должен выводить:
True
False"""


# variant 1:
def is_correct_bracket(text):
    start = '('
    end = ')'
    while len(text) > 0:
        if start in text and end in text:
            if text[0] == start:
                text = text.replace(start, '', 1)
                text = text.replace(end, '', 1)
            else:
                return False
        else:
            return False
    else:
        return True


print(is_correct_bracket(input()))


# variant 2:
# def is_correct_bracket(text):
#     count = 0
#     for c in text:
#         if count < 0:
#             return False
#         if c == '(':
#             count += 1
#         elif c == ')':
#             count -= 1
#     return count == 0
#
#
# print(is_correct_bracket(input()))
