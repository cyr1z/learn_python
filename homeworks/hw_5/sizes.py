# Написать функцию перевода размеров женского белья из международного во все остальные.
# Внyтри функции нужно просто обращаться к правильно составленному словарю.


sizes = dict(XXS={"RU": 42, "GR": 36, "US": 8, "FR": 38, "UK": 24, "waist": "63 - 65", "hips": "89 - 92"},
             XS={"RU": 44, "GR": 38, "US": 10, "FR": 40, "UK": 26, "waist": "66 - 69", "hips": "93 - 96"},
             S={"RU": 46, "GR": 40, "US": 12, "FR": 42, "UK": 28, "waist": "70 - 74", "hips": "97 - 101"},
             M={"RU": 46, "GR": 42, "US": 14, "FR": 44, "UK": 30, "waist": "75 - 78", "hips": "102 - 104"},
             L={"RU": 50, "GR": 44, "US": 16, "FR": 46, "UK": 32, "waist": "79 - 83", "hips": "105 - 108"},
             XL={"RU": 52, "GR": 46, "US": 18, "FR": 48, "UK": 34, "waist": "84 - 89", "hips": "109 - 112"},
             XXL={"RU": 54, "GR": 48, "US": 20, "FR": 50, "UK": 36, "waist": "90 - 94", "hips": "113 - 117"},
             XXXL={"RU": 56, "GR": 50, "US": 22, "FR": 52, "UK": 38, "waist": "95 - 97", "hips": "118 - 122"})


def size_transcode(size, standard):
    return f'{size} = {standard} {sizes[size].get(standard)} ' \
           f'(waist: {sizes[size].get("waist")}, hips: {sizes[size].get("hips")})'


def get_digit(welcome_string='Enter the number: '):
    line = ''
    while not line.isdigit():
        line = input(welcome_string)
    return int(line)


def input_select_from_list(my_list, name='item'):
    print(f"select your {name}")
    for i, item in enumerate(my_list):
        print(i, item, sep=': ')
    k = get_digit(f"input {name} number: ")
    while k not in range(len(my_list)):
        k = get_digit(f"input {name} number: ")
    return my_list[k]


if __name__ == '__main__':
    international_sizes = [i for i in sizes.keys()]
    standards = list(filter(lambda x: x != 'waist' and x != 'hips', [i for i in sizes.values()][0].keys()))
    my_size = input_select_from_list(international_sizes, name='size')
    my_st = input_select_from_list(standards, name='standard')
    print(size_transcode(my_size, my_st))
