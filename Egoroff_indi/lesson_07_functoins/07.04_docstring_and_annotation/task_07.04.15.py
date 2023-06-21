""" Напишите функцию shift_letter , которая принимает два аргумента:
letter одна английская буква в нижнем регистре
shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift .Сдвиг может быть цикличным в
пределах от a до z. Ниже примеры:
shift_letter('b', 2)=> 'd'
shift_letter('d', 1) => 'e'
shift_letter('z', 1) => 'a'
shift_letter('d', -2) => 'b'
shift_letter('d', 26) => 'd'
shift_letter('b', -3) => 'y'
    Не забудьте проаннотировать аргументы и также добавьте doc-строку «Функция сдвигает символ letter на shift позиций»
    Функция shift_letter  должна вернуть новый символ. Вот вам в помощь ascii коды английских буквы, вам нужны только
символы в нижнем регистре
    Нужно написать только определение функции shift_letter """


# variant 1:
def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    offset = ord(letter) + shift
    while offset < 97 or offset > 122:
        if offset > 122:
            offset -= 26
        elif offset < 97:
            offset += 26
    result = chr(offset)
    return result


# variant 2:
# def shift_letter(b: str, s: int) -> str:
#     '''Функция сдвигает символ letter на shift позиций'''
#     return chr((ord(b) - 97 + s) % 26 + 97)

assert shift_letter('b', 2) == 'd'
assert shift_letter('d', 1) == 'e'
assert shift_letter('z', 1) == 'a'
assert shift_letter('d', -2) == 'b'
assert shift_letter('d', 26) == 'd'
assert shift_letter('b', -3) == 'y'
assert shift_letter('z', 5) == 'e'
assert shift_letter('w', 28) == 'y'
assert shift_letter('w', -26) == 'w'
assert shift_letter('w', -27) == 'v'
assert shift_letter('a', 53) == 'b'
print('OK')
