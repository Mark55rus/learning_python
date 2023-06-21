""" Пользуясь вложенными функциями, реализуйте простой калькулятор.
    Необходимо реализовать функцию calculate, которая принимает три параметра:
- обязательный числовой параметр x
- обязательный числовой параметр y
- необязательный строковый параметр operation, по умолчанию принимает значение английской буквы a
    В данной функции должны быть реализованы следующие функции:
- addition - печатаем сложение двух чисел,
- subtraction - печатаем вычитание из первого переданного параметра второго;
- division - печатаем деление первого на второго.
- multiplication - печатаем умножение двух чисел.
    Каждая из этих четырёх вложенных функций должна распечатать результат математической операции и ничего не
возвращать.
    А при помощи параметра operation и условного оператора нужно выбрать какая из функций должна быть вызвана:
если operation = a, вызываем функцию addition;
если operation = s, вызываем функции subtraction;
если operation = d, вызываем функции division;
если operation = m, вызываем функции multiplication;
calculate(2, 5) # Печатает 7.0
calculate(2.2, 15, 'a') # Печатает 17.2
calculate(22, 15, 's') # Печатает 7.0
calculate(2, 3.2, 'm') # Печатает 6.4
calculate(10, 0.4, 'd') # Печатает 25.0
    Если operation принимает значение, отличное от перечисленных выше букв, то необходимо вывести на экран сообщение
Ошибка. Данной операции не существует. Также если мы выполняем деление, то второе число (y) не должен равняться нулю, в
противном случае необходимо вывести на экран: На ноль делить нельзя!"""

def calculate(x: float, y: float, operation: str = 'a') -> None:
    def addition():
        print(float(x + y))

    def subtraction():
        print(float(x - y))

    def division():
        print(x / y if y != 0 else 'На ноль делить нельзя!')

    def multiplication():
        print(float(x * y))

    match operation:
        case 'a':
            addition()
        case 's':
            subtraction()
        case 'd':
            division()
        case 'm':
            multiplication()
        case _:
            print('Ошибка. Данной операции не существует')


calculate(2, 5)  # Печатает 7.0
calculate(2.2, 15, 'a')  # Печатает 17.2
calculate(22, 15, 's')  # Печатает 7.0
calculate(2, 3.2, 'm')  # Печатает 6.4
calculate(10, 0.4, 'd')  # Печатает 25.0


# variant 2:
# def calculate(x: float, y: float, operation: str = 'a') -> None:
#     match operation:
#         case 'a': addition = lambda x, y: x + y; print(addition(x, y))
#         case 's': subtraction = lambda x, y: x - y;  print(subtraction(x, y))
#         case 'm': multiplication = lambda x, y: x * y; print(multiplication(x, y))
#         case 'd': division = lambda x, y: x / y; print(division(x, y) if y else 'На ноль делить нельзя!')
#         case _: print('Ошибка. Данной операции не существует')
