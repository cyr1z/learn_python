import os
from datetime import datetime as dt


class LogError(Exception):
    def __init__(self, ex=0):
        if ex and isinstance(ex, Exception):
            print(f'log error: {str(ex.__class__.__name__)} {str(ex)}')

    pass


class Log:
    def __init__(self, logfile):
        self.logfile = logfile

    def __add__(self, other):
        self.add_exception(other)

    @staticmethod
    def print_error(e):
        if e and isinstance(e, Exception):
            print(f'log error: {str(e.__class__.__name__)} {str(e)}')

    def add_string(self, string):
        try:
            with open(self.logfile, "a") as f:
                f.write(f'{dt.now().strftime("%x: %X")} {str(string)}\n')
        except EnvironmentError as ee:
            raise LogError(ee)

    def add_exception(self, e):
        if not isinstance(e, Exception):
            self.add_string(e)
        else:
            try:
                with open(self.logfile, "a") as f:
                    f.write(f'{dt.now().strftime("%x: %X")} {str(e.__class__.__name__)} {str(e)} \n')
            except EnvironmentError as ee:
                raise LogError(ee)

    def __str__(self):
        try:
            with open(self.logfile, "r") as f:
                return ''.join(f.readlines())
        except FileNotFoundError:
            return None
        except EnvironmentError as ee:
            self.print_error(ee)
            return None

    def __repr__(self):
        return f'logging to -> {self.logfile}'

    def clear(self):
        print('log clear')
        os.remove(self.logfile)

    def tail(self, line_count=1):
        try:
            with open(self.logfile, "r") as f:
                return ''.join(f.readlines()[-line_count:])
        except FileNotFoundError:
            return None
        except EnvironmentError as ee:
            self.print_error(ee)
            return None
