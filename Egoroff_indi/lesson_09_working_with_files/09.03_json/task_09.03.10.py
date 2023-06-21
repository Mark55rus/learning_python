""" Анализ продаж.
    К вам в руки попал файлик формата json, в котором содержится информация одного автосалона о продажах менеджеров.
В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого
автомобиля.
    Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж. В качестве
ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж."""

import json

name = ''
last_name = ''
total_sales = 0
with open("task_09.03.10.json") as file:
    data = json.load(file)
for item in data:
    sales = 0
    for car in item["cars"]:
        sales += car["price"]
    if sales > total_sales:
        name = item["manager"]["first_name"]
        last_name = item["manager"]["last_name"]
        total_sales = sales
print(name, last_name, total_sales)
