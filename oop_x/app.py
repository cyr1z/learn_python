import os
from settings import LOGFILE
from logger import Log

from main import main
from models import Programmer, Recruiter, Vacancy, Candidate

if __name__ == '__main__':
    log = Log(LOGFILE)
    try:
        main()
    except Exception as e:
        try:
            log.add_exception(e)
        except FileNotFoundError as fe:
            print(f'log error: {str(fe.__class__.__name__)} {str(fe)} \n')
        except IOError as fe:
            print(f'log error: {str(fe.__class__.__name__)} {str(fe)} \n')

    if os.path.exists('emails.txt'):
        os.remove('emails.txt')

    print(log.tail(3))
