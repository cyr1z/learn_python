# 7. Write a Python class to implement pow(x, n).


class Pow:
    def __init__(self, num, my_pow):
        self.num = num
        self.pow = my_pow

    def to_power(self, num, pw):
        if pw == 1:
            return num
        elif pw == 0:
            return 1
        elif pw < 0:
            return 1 / self.to_power(num, pw * -1)
        else:
            return num * self.to_power(num, pw - 1)

    def power(self):
        return self.to_power(self.num, self.pow)


a = Pow(2, -2)

print(a.power())
