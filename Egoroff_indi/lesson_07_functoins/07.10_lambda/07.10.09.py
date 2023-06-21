""" Хорошо постарались с прошлой задачей! Однако мы забыли, что скидка должна быть только для тех товаров, стоимость
которых больше 50. Вам стоит внести это изменение в прошлый код
    Ваша задача только переопределить переменную sale_lambda """

sale_lambda = lambda x: x * 0.9 if x > 50 else x

assert sale_lambda(1) == 1
assert sale_lambda(100) == 90.0
assert sale_lambda(-1) == -1
assert sale_lambda(-100) == -100
assert sale_lambda(50) == 50
assert sale_lambda(60) == 54.0
assert sale_lambda(12.33) == 12.33
print('Process finished')
