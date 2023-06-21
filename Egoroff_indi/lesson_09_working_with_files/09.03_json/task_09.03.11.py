""" В json-файле содержится информация о нескольких групп людей, при этом у каждой группы есть свой идентификатор.
    Ваша задача скачать файлик и самостоятельно найти идентификатор группы, в которой находится самое большое количество
женщин, рожденных после 1977 года. В качестве ответа необходимо указать через пробел идентификатор найденной группы и
сколько в ней было женщин, рожденных после 1977 года."""

import json

search_id = 0
count_female = 0
with open("task_09.03.11.json") as file:
    data = json.load(file)
for item in data:
    count = 0
    for female in item["people"]:
        if female["gender"] == 'Female' and female["year"] > 1977:
            count += 1
    if count > count_female:
        count_female = count
        search_id = item["id_group"]
print(search_id, count_female)
