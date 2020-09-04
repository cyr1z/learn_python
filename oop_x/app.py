import os
from settings import LOGFILE, TAILDEF
from logger import Log, LogError
from main import main

if __name__ == '__main__':
    log = Log(LOGFILE)
    try:
        main()
    except LogError:
        pass
    except Exception as e:
        try:
            log.add_exception(e)
        except LogError:
            pass
        except FileNotFoundError as fe:
            print(f'log error: {str(fe.__class__.__name__)} {str(fe)} \n')
        except IOError as fe:
            print(f'log error: {str(fe.__class__.__name__)} {str(fe)} \n')

    if os.path.exists('emails.txt'):
        os.remove('emails.txt')

    print(log.tail(TAILDEF))
