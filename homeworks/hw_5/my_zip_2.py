# Разбираемся, что делает функция zip, и пробуем написать свой собственный zip.


def my_sweet_zip(*args):
    return list(map(lambda j: tuple(i[j] for i in list(args)), range(len(sorted(args, key=len)[0]))))


if __name__ == '__main__':
    a, b, c = [1, 2, 7, 4], [11, 12, 33], [55, 52, 54]
    print(my_sweet_zip(a, b, c))
    print(list(zip(a, b, c)))
