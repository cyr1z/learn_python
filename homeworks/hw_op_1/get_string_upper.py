class StringInOut:
    string = ''

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


a = StringInOut()
a.get_string()
a.print_string()
