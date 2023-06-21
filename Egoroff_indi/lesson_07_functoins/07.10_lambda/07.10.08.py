""" Имеется функция sale, которая возвращает цену товара со скидкой 10%.
def sale(x):
    return x*0.9
    Однако мы изучаем анонимные функции, поэтому на основе данной функции создайте анонимную функцию и присвойте её
переменной sale_lambda"""

sale_lambda = lambda x: x * 0.9

assert sale_lambda(1) == 0.9
assert sale_lambda(100) == 90.0
assert sale_lambda(-1) == -0.9
assert sale_lambda(-100) == -90.0
print('Process finished')
