import sys


def fizz_buzz(fizz, buzz, end_number):
    my_result = []
    for i in range(1, end_number + 1):
        if not i % fizz and not i % buzz:
            my_result.append('FB')
        elif not i % fizz:
            my_result.append('F')
        elif not i % buzz:
            my_result.append('B')
        else:
            my_result.append(str(i))
    return ' '.join(my_result)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        fileexport = sys.argv[2]
    else:
        filename = "data.txt"
        fileexport = "export.txt"

    f = open(filename, 'r')
    ef = open(fileexport, 'w')
    for line in f:
        m = line.split()
        int_m = [int(h) for h in m]
        ef.write(fizz_buzz(*int_m) + '\n')

    ef.close()
    f.close()
