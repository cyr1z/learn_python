# Написать функцию перевода размеров женского белья из международного во все остальные.
# Внyтри функции нужно просто обращаться к правильно составленному словарю.


sizes = dict(XXS={"RU": 42, "GR": 36, "US": 8, "FR": 38, "UK": 24},
             XS={"RU": 44, "GR": 38, "US": 10, "FR": 40, "UK": 26},
             S={"RU": 46, "GR": 40, "US": 12, "FR": 42, "UK": 28},
             M={"RU": 46, "GR": 42, "US": 14, "FR": 44, "UK": 30},
             L={"RU": 50, "GR": 44, "US": 16, "FR": 46, "UK": 32},
             XL={"RU": 52, "GR": 46, "US": 18, "FR": 48, "UK": 34},
             XXL={"RU": 54, "GR": 48, "US": 20, "FR": 50, "UK": 36},
             XXXL={"RU": 56, "GR": 50, "US": 22, "FR": 52, "UK": 38})

if __name__ == '__main__':
    size = ''
    standard = ''

    while size not in sizes.keys():
        size = input("input size: ")

    while standard not in list(sizes.values())[0].keys():
        standard = input("input standard: ")

    print(size, '=', standard, sizes[size][standard])
