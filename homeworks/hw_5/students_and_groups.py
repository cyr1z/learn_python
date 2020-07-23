# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент
# (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

from faker import Faker
from random import randint, choices

fake = Faker('uk_UA')


def dict_to_string(my_dict, pre_string=''):
    return '\n'.join(map(lambda i: f'{pre_string}{i}: {my_dict[i]}', my_dict)).strip()


def two_or_more_groups(my_dict):
    return dict(filter(lambda e: len(e[1]) > 1, my_dict.items()))


def frontend_group(my_dict):
    return dict(filter(lambda e: 'FrontEnd' in e[1], my_dict.items()))


def python_and_java_groups(my_dict):
    return dict(filter(lambda e: 'Python' in e[1] or 'Java' in e[1], my_dict.items()))


if __name__ == '__main__':
    groups = ["Python", "FrontEnd", "FullStack", "Java"]
    students = {fake.name(): set(choices(groups, k=randint(1, len(groups)))) for i in range(20)}

    print(dict_to_string(students), '\n')

    print(dict_to_string(two_or_more_groups(students)), '\n')

    print(dict_to_string(frontend_group(students)), '\n')

    print(dict_to_string(python_and_java_groups(students)), '\n')
