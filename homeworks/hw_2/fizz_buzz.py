def fizz_buzz(fizz, buzz, end_number):
    my_result_string = ""
    for i in range(1, end_number + 1):
        if not i % fizz and not i % buzz:
            my_result_string += 'FB'
        elif not i % fizz:
            my_result_string += 'F'
        elif not i % buzz:
            my_result_string += 'B'
        else:
            my_result_string += str(i)
        my_result_string += ' '
    return my_result_string


def get_digit(welcome_string='Enter the number: '):
    line = ''
    while not line.isdigit():
        line = input(welcome_string)
    return int(line)


if __name__ == '__main__':
    fizz_num = get_digit('Enter the fizz: ')
    buzz_num = get_digit('Enter the buzz: ')
    end_num = get_digit('Enter the end number: ')
    print('\n', fizz_buzz(fizz_num, buzz_num, end_num))
