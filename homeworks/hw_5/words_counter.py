# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!


# from string import ascii_letters
# from collections import Counter

filename = 'text.txt'


def get_clean_string(my_string):
    # allowed_charset = set(ascii_letters + " ")
    # return ''.join(filter(lambda x: x in allowed_charset, my_string))
    return ''.join(filter(lambda x: x.isidentifier() or x.isspace(), my_string))


def dict_to_string(my_dict, pre_string=''):
    return ''.join(map(lambda i: f'{pre_string} "{i}": {my_dict[i]}\n', my_dict)).strip()


def items_counter(my_dict):
    items_set = list(set(my_dict))
    items_set.sort()
    # result_dict = {i: my_dict.count(i) for i in items_set}
    # result_dict = Counter(my_dict)
    return dict(map(lambda i: (i, my_dict.count(i)), items_set))


def word_counter(dirty_string):
    clean_string = get_clean_string(dirty_string)
    clean_string = clean_string.lower()
    words_list = clean_string.split()
    return items_counter(words_list)


if __name__ == '__main__':
    f = open(filename, 'r')
    big_string = f.read()
    print(dict_to_string(word_counter(big_string), 'count of'))
    f.close()
