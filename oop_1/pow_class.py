class Pow:
    def __init__(self, num, my_pow):
        self.num = num
        self.pow = my_pow

    def to_power(self, num, idx):
        if (idx == 1):
            return (num)
        else:
            return (num * self.to_power(num, idx - 1))

    def power(self):
        return self.to_power(self.num, self.pow)


a = Pow(2, 2)

print(a.power())
