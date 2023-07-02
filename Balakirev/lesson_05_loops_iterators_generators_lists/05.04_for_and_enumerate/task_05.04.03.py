""" Подвиг 2. Вводится строка с номером телефона. Ожидается формат ввода:
+7(xxx)xxx-xx-xx
где x - это цифра. Размер введенных символов считается верным (то есть, не
может быть, чтобы отсутствовала какая-либо цифра или была лишняя). Необходимо
проверить, что введенная строка соответствует этому формату. Вывести ДА, если
соответствует и НЕТ - в противном случае."""

s = '+7(xxx)xxx-xx-xx'
n = input().rjust(len(s))
for i, item in enumerate(n):
    if (s[i] == item and item != 'x') or (s[i] == 'x' and item.isdigit()):
        continue
    print('НЕТ')
    break
else:
    print('ДА')
