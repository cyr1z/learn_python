from datetime import datetime
import csv
from logger import Log
from settings import LOGFILE, CSVFILE

log = Log(LOGFILE)


class UnableToWorkException(Exception):
    pass


class Employee:

    def validate_user_email_exist(self):
        with open('emails.txt', 'r') as f:
            emails_from_file = (x.strip() for x in f.readlines())
            if self.mail in emails_from_file:
                raise ValueError

    def write_emails_to_file(self):
        if self.mail:
            with open("emails.txt", "a") as f:
                f.write(self.mail + '\n')

    def __init__(self, name, surname, mail, phone, money_per_day):
        try:
            name = name.capitalize()
        except AttributeError:
            name = str(name).capitalize()
        except NameError as e:
            log.add_string(f' create employe error with name {name}')
            log.add_exception(e)
            raise
        self.name = name

        try:
            surname = name.capitalize()
        except AttributeError:
            surname = str(name).capitalize()
        except NameError as e:
            log.add_string(f' create employe error with name {surname}')
            log.add_exception(e)
            raise
        self.surname = surname

        self.mail = mail
        try:
            self.validate_user_email_exist()
        except ValueError:
            print('this email is busy')
            raise
        except FileNotFoundError:
            pass
        self.write_emails_to_file()
        self.phone = phone
        self.money_per_day = money_per_day

    @property
    def about_person(self):
        return f'{self.__class__.__name__}, {self.name} {self.surname}, {self.weekdays()} '

    @staticmethod
    def weekdays():
        now = datetime.now()
        return sum(1 for day in range(1, now.day + 1) if datetime(now.year, now.month, day).weekday() < 5)

    def work(self):
        return "I come to the office"

    def check_salary(self, days=0):
        if not days:
            days = self.weekdays()
        return days * self.money_per_day

    def __gt__(self, other):
        return self.money_per_day > other.money_per_day

    def __lt__(self, other):
        return self.money_per_day < other.money_per_day

    def __ge__(self, other):
        return self.money_per_day >= other.money_per_day

    def __le__(self, other):
        return self.money_per_day <= other.money_per_day


class Recruiter(Employee):
    hired_this_month = []

    def work(self):
        return super().work() + ' and start hiring'

    def __str__(self):
        return f'Recruiter: {self.name} {self.surname}'

    def __repr__(self):
        return self.__str__() + f'. Hired this month: {", ".join(self.hired_this_month)}'


class Programmer(Employee):
    closed_this_month = []

    def __init__(self, tech_stack, *args):
        self.tech_stack = tech_stack
        super().__init__(*args)

    def work(self):
        return super().work() + ' and start coding'

    def __gt__(self, other):
        if not isinstance(other, Programmer):
            return super().__gt__(other)
        return len(self.tech_stack) > len(other.tech_stack)

    def __lt__(self, other):
        if not isinstance(other, Programmer):
            return super().__lt__(other)
        return len(self.tech_stack) < len(other.tech_stack)

    def __ge__(self, other):
        if not isinstance(other, Programmer):
            return super().__ge__(other)
        return len(self.tech_stack) >= len(other.tech_stack)

    def __le__(self, other):
        if not isinstance(other, Programmer):
            return super().__le__(other)
        return len(self.tech_stack) <= len(other.tech_stack)

    def __add__(self, other):
        result = Programmer(set(self.tech_stack + other.tech_stack),
                            f'{self.name} and {other.name},',
                            f'{self.surname} and {other.surname}',
                            '', '', self.money_per_day + other.money_per_day)
        result.closed_this_month = set(self.closed_this_month + other.closed_this_month)
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f'Programmer: {self.name} {self.surname} ({", ".join(self.tech_stack)})'

    def __repr__(self):
        return self.__str__() + f'  day salary: {self.money_per_day}, \n ' \
                                f'clothed this month: {", ".join(self.closed_this_month)}'


class Candidate:
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill_grade = main_skill_grade
        self.main_skill = main_skill

    @classmethod
    def make_candidates_from_csv(cls, filename=CSVFILE):
        with open(filename) as f_obj:
            lines = csv.DictReader(f_obj)
            return [Candidate(l['Full Name'], l['Email'], l['Technologies'].split('|'), l['Main Skill'],
                              l['Main Skill Grade']) for l in lines]

    def work(self):
        raise UnableToWorkException(f'Candidate {self.full_name} ({self.main_skill}): I`m not '
                                    f'hired yet, lol.')

    def __str__(self):
        return f'Candidate: {self.full_name} {", ".join(self.technologies)}, ' \
               f'{self.main_skill}: {self.main_skill_grade}'

    def __repr__(self):
        return self.__str__()


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return f'Vacancy: {self.title} {self.main_skill}: {self.main_skill_level}'

    def __repr__(self):
        return self.__str__()
