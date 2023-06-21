""" В переменную adding_10 присвойте lambda функцию, которая принимает одно число и увеличивает его на 10.
Ничего кроме создания переменной adding_10 делать не нужно"""

adding_10 = lambda x: x + 10

assert adding_10(10) == 20
assert adding_10(-10) == 0
assert adding_10(0) == 10
assert adding_10(2.0) == 12.0

print("Process finished")
