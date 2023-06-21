"""Магазин канцелярских товаров.
    Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров. Известно, что цена
ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера. Также известно, что стоимость карандаша
составляет 3 рубля. Требуется определить общую стоимость покупки."""

pencils, pens, markers = map(int, input().split())
price_pencil = 3
price_pen = price_pencil + 2
price_marker = price_pen + 7
print(pencils * price_pencil + pens * price_pen + markers * price_marker)
