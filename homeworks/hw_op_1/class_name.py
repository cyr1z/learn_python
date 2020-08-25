class AmazingClass:
    def get_name(self):
        return self.__class__.__name__

a = AmazingClass()
print(a.get_name())