""" Находим первый дубль.
    Напишите функцию first_repeated_word , которая принимает строку, состоящую из нескольких слов, слова разделяются
между собой пробелом. Функция должна найти первое повторяющееся слово и вернуть его в качестве результата. Если передана
строка, в которой все слова различны, функция first_repeated_word должна вернуть None.
Регистр букв при сравнении нужно учитывать.
first_repeated_word("ab ca bc ab") => "ab"
first_repeated_word("ab ca bc Ab cA aB bc") => "bc"
first_repeated_word("ab ca bc ca ab bc") => "ca"
first_repeated_word("ab ca bc") => None
Для функции first_repeated_word нужно добавить док-строку  "Находит первый дубль в строке"
и не забудьте проаннотировать аргументы и возврат функции
Нужно написать только определение функции first_repeated_word """


def first_repeated_word(text: str) -> str | None:
    """Находит первый дубль в строке"""
    temp = set()
    for word in text.split():
        if word in temp:
            return word
        temp.add(word)
    return None
