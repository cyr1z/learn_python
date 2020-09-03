import os
from datetime import datetime as dt


class Log:
    def __init__(self, logfile):
        self.logfile = logfile

    def __add__(self, other):
        self.add_exception(other)

    def add_string(self, string):
        with open(self.logfile, "a") as f:
            f.write(f'{dt.now().strftime("%x: %X")} {str(string)}\n')

    def add_exception(self, e):
        if not isinstance(e, Exception):
            self.add_string(e)
        else:
            with open(self.logfile, "a") as f:
                f.write(f'{dt.now().strftime("%x: %X")} {str(e.__class__.__name__)} {str(e)} \n')

    def __str__(self):
        with open(self.logfile, "r") as f:
            return ''.join(f.readlines())

    def __repr__(self):
        return f'logging to -> {self.logfile}'

    def clear(self):
        print('log clear')
        os.remove(self.logfile)
