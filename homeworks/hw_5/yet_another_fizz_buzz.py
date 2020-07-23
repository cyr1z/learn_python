# украшаем работу физбазов работой со строками, списками, пробуем генераторы списков и прочие новые красоты,
# которые выучили.

import sys
from functools import reduce


def get_fizz_buzz_or_number(fizz, buzz, num):
    r = 'FB' if not num % fizz and not num % buzz else 'F' if not num % fizz else 'B' if not num % buzz else str(num)
    return r


def fizz_buzz(fizz, buzz, end_number):
    # return ' '.join([get_fizz_buzz_or_number(fizz, buzz, i) for i in range(1, end_number + 1)])
    return ' '.join(list(map(lambda x: get_fizz_buzz_or_number(fizz, buzz, x), range(1, end_number + 1))))


def get_filenames():
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    return "data.txt", "export.txt"


max_line_count = 20

if __name__ == '__main__':
    filename, file_export = get_filenames()

    f = open(filename, 'r')
    ef = open(file_export, 'w')

    for line_number, line in enumerate(f, 1):

        if line_number > max_line_count:
            print(f"No more {max_line_count} lines")
            break

        split_line = line.split()

        if len(split_line) != 3:
            print(f'wrong line {line_number} in file {filename}: "{line.strip()}"')
            continue

        # if not all(list(map(lambda x: x.isdigit(), split_line))):
        if not reduce(lambda y, x: y and x.isdigit(), split_line, True):
            print(f'wrong line {line_number} in file {filename}: "{line.strip()}"')
            continue

        # fizz_buzz_n = [int(h) for h in split_line]
        fizz_buzz_n = map(int, split_line)
        ef.write(fizz_buzz(*fizz_buzz_n) + '\n')

    ef.close()
    f.close()
