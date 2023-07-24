""" Подвиг 3. Объявите функцию, которая принимает строку на кириллице и
преобразовывает ее в латиницу, используя следующий словарь для замены
русских букв на соответствующее латинское написание.
    Функция должна возвращать преобразованную строку. Замены делать без учета
регистра (исходную строку перевести в нижний регистр - малые буквы).
    Определите декоратор с параметром chars и начальным значением " !?",
который данные символы преобразует в символ "-" и, кроме того, все подряд
идущие дефисы (например, "--" или "---") приводит к одному дефису. Полученный
результат должен возвращаться в виде строки.
    Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите
декорированную функцию для введенной строки s:

s = input()

Результат отобразите на экране."""
from functools import wraps

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
     'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
     'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
     'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
     'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def args_decorator(chars=" !?"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result: str = func(*args, **kwargs)
            for char in result:
                if char in chars:
                    result = result.replace(char, "-")
            while "--" in result:
                result = result.replace("--", "-")
            return result

        return wrapper

    return decorator


@args_decorator(chars="?!:;,. ")
def translate(text):
    translated_text = ""
    for char in text.lower():
        translated_text += t.get(char, char)
    return translated_text


s = input()
print(translate(s))
