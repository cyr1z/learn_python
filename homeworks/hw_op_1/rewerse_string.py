class ReverseWords:
    def __init__(self,string):
        self.string = string
        self.reverse = ' '.join(reversed(string.split()))
        
    def __str__(self):
        return self.reverse

print(ReverseWords('Happy New year'))