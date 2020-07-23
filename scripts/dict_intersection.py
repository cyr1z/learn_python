# обнаружил, что dict.keys() имеет отдельный тип, и работает как set
# написал функцию пересечения словарей, для одинаковых пар ключ - значение, либо для совпадеения только по ключу


def dict_intersection(a, b, confirm_values=True):
    d = {}
    d.update(a)
    d.update(b)
    if confirm_values:
        return dict(filter(lambda e: e[0] in a.keys() & b.keys() and a[e[0]] == b[e[0]], d.items()))
    return dict(filter(lambda e: e[0] in a.keys() & b.keys(), d.items()))


if __name__ == '__main__':
    dict_a = {1: 2, 3: 6, 4: 9, "t": [7, 6, 4]}
    dict_b = {3: 6, 7: 2, 4: 5, "t": [7, 6, 4]}
    print(dict_intersection(dict_a, dict_b))
    print(dict_intersection(dict_a, dict_b, confirm_values=False))
