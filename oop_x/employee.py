from datetime import datetime


class Employee:
    def __init__(self, name, surname, mail, phone, money_per_day):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.mail = mail
        self.phone = phone
        self.money_per_day = money_per_day

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


vasilyev = Programmer(['js', 'python', 'make good coffee'], 'Vasya', 'Vasilyev', 'ad@hell.oj', '+322223322', 32)
gunko = Programmer(['js', 'python', 'kubernetes', 'docker'], 'petr', 'gunko', 'ur@hell.oj', '+322227772', 30)
tatarinova = Recruiter('Lena', 'Tatarinova', 'hop@hell.oj', '+372223322', 32)

print(vasilyev, gunko, tatarinova, sep='\n')
print(f'{vasilyev.name} salary: {vasilyev.check_salary()}')
print(vasilyev.surname, 'said:', vasilyev.work())
print(vasilyev > tatarinova)
print(vasilyev >= tatarinova)
print(vasilyev.tech_stack)
print(gunko)
print(vasilyev < gunko)
print(vasilyev + gunko)
