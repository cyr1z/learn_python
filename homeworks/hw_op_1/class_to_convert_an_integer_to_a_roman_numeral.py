class RomanNumber:
    """
    Convert integer to roman number and roman to integer
    self.integer : decimal number
    self.get_roman() : return roman number string
    """
    roman_registers = (('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M',))
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, num):
        if isinstance(num, int) or str(num).isdigit():
            try:
                self.integer = int(num)
            except ValueError:
                print('wrong integer')
                exit()
        else:
            try:
                self.integer = self.roman_to_int(num)
            except ValueError:
                print('wrong string')
                exit()

    @staticmethod
    def __get_roman_notation__(x):
        """
        returns a Roman notation string for a digit using
        the passed list of case-matching Roman numerals
        :param x: (9, ('I', 'V', 'X'))
        :return: 'IX'
        """
        if x[0] < 4:
            return x[1][0] * x[0]
        elif x[0] == 4:
            return x[1][0] + x[1][1]
        elif x[0] < 9:
            return x[1][1] + x[1][0] * (x[0] - 5)
        return x[1][0] + x[1][2]

    def get_roman(self):
        """
        convert decimal number to romanian for 0 - 3999
        :return: Roman numeral string('CLIX')
        """

        if self.integer > 3999:
            return 'bigger number'
        x = str(self.integer)
        x_register_list = tuple(map(int, x.strip()))
        pair_registers = tuple(zip(x_register_list[::-1], self.roman_registers))
        return ''.join(tuple(map(self.__get_roman_notation__, pair_registers))[::-1])

    def get_int(self):
        return self.integer

    def roman_to_int(self, num):
        """
        Convert roman to int
        :param num: roman number string 'XXXL'
        :return: int decimal number
        """
        result = 0
        for i, val in enumerate(num):
            if (i + 1) == len(num) or self.roman_numerals[val] >= self.roman_numerals[num[i + 1]]:
                result += self.roman_numerals[val]
            else:
                result -= self.roman_numerals[val]
        return result

    def __str__(self):
        return self.get_roman()

    def __repr__(self):
        return self.get_roman()


if __name__ == '__main__':
    a = RomanNumber(10)
    b = RomanNumber(312)
    c = 2014
    d = 3999
    xl = RomanNumber('XL')

    print(f'{a.integer} is roman {a}')  # 10 is roman X
    print(f'{b.integer} is roman {b}')  # 312 is roman CCCXII
    print(f'{c} is roman {RomanNumber(c).get_roman()}')  # 2014 is roman MMXIV
    print(f'{d} is roman {RomanNumber(d)}')  # 3999 is roman MMMCMXCIX
    print(f'{4000} is roman {RomanNumber(4000)}')  # 4000 is roman bigger number
    print(f'{xl} is arabic {xl.integer}')  # XL is arabic 40
