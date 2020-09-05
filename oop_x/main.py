from models import Candidate, Programmer, Recruiter, Vacancy
# from logger import LogError


def main():
    vasilyev = Programmer(['js', 'python', 'make good coffee'],
                          'Vasya', 'Vasilyev',
                          'ad@hell.oj', '+322223322', 32,
                          )

    gunko = Programmer(['js', 'python', 'kubernetes', 'docker'], 'petr', 'gunko', 'ur@hell.oj', '+322227772', 30)

    tatarinova = Recruiter('Lena', 'Tatarinova', 'hop@hell.oj', '+372223322', 32)
    gagarin = Candidate('Yuriy Gagarin', 'yuriy@gagarin.su', ['spaceman', 'pilot'], 'pilot', 100)
    peterson = Candidate('Jim Peterson', 'jim_peterson.gmail.com', ['python', 'js'], 'python', 79)
    vorghol = Candidate('Anastasia Vorghol', 'vorghol_a1952.gmail.com', ['python', 'js'], 'js', 68)
    js_junior = Vacancy('JS Junior', 'js', 45)
    python_middle = Vacancy('Python Middle', 'python', 60)

    print(vasilyev, gunko, tatarinova, sep='\n')
    print(f'{vasilyev.name} salary: {vasilyev.check_salary()}')
    print(vasilyev.surname, 'said:', vasilyev.work())
    print(vasilyev > tatarinova)
    print(vasilyev >= tatarinova)
    print(vasilyev.tech_stack)
    print(gunko)
    print(vasilyev < gunko)
    print(vasilyev + gunko)
    print(js_junior)
    print(peterson)
    print(vorghol)
    print(gagarin)
    print(python_middle)
    print(vasilyev.about_person)
    data = Candidate.make_candidates_from_csv()
    [print(i) for i in data]

    # a = 1/0
    # raise ValueError
    # raise FileNotFoundError('bananiv nema')
    # ed = FileNotFoundError('azazaz')
    # raise LogError(ed)
    # vova = Candidate('vova bulochkin', 'vova.gmail.com', ['python', 'js'], 'python', 79)
    # vova.work()
