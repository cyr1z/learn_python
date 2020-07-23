# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

from faker import Faker
from random import randint

fake = Faker('uk_UA')


def dict_to_string(my_dict, pre_string=''):
    return '\n'.join(map(lambda i: f'{pre_string}{i}: {my_dict[i]}', my_dict)).strip()


def mid_scores(my_dict, rev=False):
    mid_dict = {a: sum(b)/len(b) for a, b in my_dict.items()}
    sorted_dict = {a: b for a, b in sorted(mid_dict.items(), key=lambda i: i[1], reverse=rev)}
    return sorted_dict


def best_student(my_dict):
    name = list(mid_scores(my_dict))[-1]
    mid_score = mid_scores(my_dict).get(name)
    return name, mid_score, my_dict.get(name)


def bad_student(my_dict):
    name = list(mid_scores(my_dict))[0]
    mid_score = mid_scores(my_dict).get(name)
    return name, mid_score, my_dict.get(name)


def student_to_string(name, mid_score, scores):
    return f'{name} average score: {mid_score}, all scores: {", ".join(str(c) for c in scores)}'


if __name__ == '__main__':
    students = {fake.name(): [randint(2, 10) for j in range(10)] for i in range(20)}
    print(dict_to_string(students), '\n')
    print('Best - ', student_to_string(*best_student(students)))
    print('Worst - ', student_to_string(*bad_student(students)))
