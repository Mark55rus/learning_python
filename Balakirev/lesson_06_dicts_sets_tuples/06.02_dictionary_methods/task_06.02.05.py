""" Подвиг 4. Имеется закодированная строка с помощью азбуки Морзе. Коды
разделены между собой пробелом. Необходимо ее раскодировать, используя
азбуку Морзе из предыдущего занятия. Полученное сообщение (строку) вывести
на экран."""

morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.',
         'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---',
         'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---',
         'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-',
         'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
         'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..',
         'ю': '..--', 'я': '.-.-', ' ': '-...-'}
back_morze = {v: k for k, v in morze.items()}
print("".join([back_morze[code] for code in input().lower().split()]))
