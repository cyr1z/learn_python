from models import Candidate
def main():
    # a = 1/0
    # raise ValueError
    # raise FileNotFoundError('bananiv nema')
    vova = Candidate('vova bulochkin', 'vova.gmail.com', ['python', 'js'], 'python', 79)
    vova.work()
