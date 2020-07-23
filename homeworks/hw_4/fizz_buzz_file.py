import sys
from functools import reduce


def fizz_buzz(fizz, buzz, end_number):
    result = []
    for i in range(1, end_number + 1):
        if not i % fizz and not i % buzz:
            result.append('FB')
        elif not i % fizz:
            result.append('F')
        elif not i % buzz:
            result.append('B')
        else:
            result.append(str(i))
    return ' '.join(result)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        file_export = sys.argv[2]
    else:
        filename = "data.txt"
        file_export = "export.txt"

    f = open(filename, 'r')
    ef = open(file_export, 'w')

    counter = 0
    for line in f:

        if counter >= 20:
            print("No more 20 lines")
            break

        counter += 1
        split_line = line.split()

        if len(split_line) != 3:
            print(f'wrong line {counter} in file {filename}: "{line.strip()}"')
            continue

        # if not all(list(map(lambda x: x.isdigit(), split_line))):
        if not reduce(lambda y, x: y and x.isdigit(), split_line, True):
            print(f'wrong line {counter} in file {filename}: "{line.strip()}"')
            continue

        fizz_buzz_n = [int(h) for h in split_line]
        ef.write(fizz_buzz(*fizz_buzz_n) + '\n')

    if counter < 20:
        print(f"We have only {counter} lines in {filename}")

    ef.close()
    f.close()
