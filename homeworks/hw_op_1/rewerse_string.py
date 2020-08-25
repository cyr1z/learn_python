# 8. Write a Python class to reverse a string word by word.


class ReverseWords:
    def __init__(self, string):
        self.string = string
        self.reverse = ' '.join(reversed(string.split()))

    def __str__(self):
        return self.reverse


print(ReverseWords('Happy New year'))
