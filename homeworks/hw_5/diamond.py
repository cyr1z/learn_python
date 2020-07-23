# Задача 2. Бриллиант
#
# Входным данным является целое число. Необходимо:
#
# написать проверку, чтобы в работу пускать только положительные нечетные числа
# для правильного числа нужно построить бриллиант из звездочек или любых других
# символов и вывести его в консоли. Для числа 1 он выглядит как одна взездочка,
# для числа три он выглядит как звезда, потом три звезды, потом опять одна,
# для пятерки - звезда, три, пять, три, одна...


def get_digit(welcome_string='Enter the number: '):
    line = ''
    while not line.isdigit():
        line = input(welcome_string)
    return int(line)


if __name__ == '__main__':
    num = get_digit()
    while not num % 2:
        num = get_digit("Enter ODD number")
    
    spaces = (num-1)//2
    top_str = '\n'.join([(num - i)//2 * ' ' + "*" * i for i in range(1, num+1, 2)])
    bottom_str = '\n'.join([(num - i)//2 * ' ' + "*" * i for i in range(num - 2, 0,  -2)])
    result = top_str.rstrip() + '\n' + bottom_str.rstrip()

    print(result)
