class IntegerToRoman:
    """
    Convert integer to roman number
    self.integer : decimal number
    self.get_roman() : return roman number string
    """

    def __init__(self, num):
        try:
            self.integer = int(num)
            if self.integer > 3999:
                print('wrong integer')
        except ValueError:
            print('wrong integer')

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
        roman_registers = (('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M',))
        x = str(self.integer)
        x_register_list = tuple(map(int, x.strip()))
        pair_registers = tuple(zip(x_register_list[::-1], roman_registers))
        return ''.join(tuple(map(self.__get_roman_notation__, pair_registers))[::-1])

    def __str__(self):
        return self.get_roman()

    def __repr__(self):
        return self.get_roman()


if __name__ == '__main__':
    a = IntegerToRoman(10)
    b = IntegerToRoman(312)

    print(f'{a.integer} is roman {a}')
    print(f'{b.integer} is roman {b}')
