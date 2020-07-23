# Задача 1. Курьер
# 
# Вам известен номер квартиры, этажность дома и количество квартир на этаже.
# Задача: написать функцию, которая по заданным параметрам напишет вам,
# в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.


def get_digit(welcome_string='Enter the number: '):
    line = ''
    while not line.isdigit():
        line = input(welcome_string)
    return int(line)


def get_floor_and_block(number, flrs, flts):
    block = 1 + number // (flts * flrs)
    floor = (number % (flts * flrs)) // flts
    return f'blok: {block} floor: {floor}'


if __name__ == '__main__':
    num = get_digit()
    floors = get_digit('how many floors? ')
    flats = get_digit('how many flats o floor? ')
    print(get_floor_and_block(num, floors,flats))
