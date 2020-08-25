# 9. Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case.


class StringInOut:
    string = ''

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


a = StringInOut()
a.get_string()
a.print_string()
