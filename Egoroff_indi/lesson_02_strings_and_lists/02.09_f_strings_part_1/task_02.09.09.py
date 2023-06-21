"""Программа запрашивает у пользователя курс доллара - вещественное число,  и также количество долларов(целое число),
которое пользователь хочет приобрести. В итоге программа должна вывести следующее сообщение:
Current dollar rate is <курс доллара>. You want to buy <количество долларов> dollars
You must pay <стоимость>"""

rate_of_dollar, quantity_dollar = float(input()), int(input())
print(f'Current dollar rate is {rate_of_dollar}. You want to buy {quantity_dollar} dollars')
print(f'You must pay {rate_of_dollar * quantity_dollar}')
