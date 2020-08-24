class Element:
    melting_point = -283
    boiling_point = -182

    @staticmethod
    def transform(t, scale):
        if scale == 'F':
            return (t - 32) * 5/9
        if scale == 'K':
            return t - 273.15
        else:
            return t

    def state_of_aggregation(self, t, scale='C'):

        t = self.transform(t, scale)

        if t < self.melting_point:
            print('solid')
        elif self.melting_point <= t <= self.boiling_point:
            print('liquid')
        else:
            print('gas')


class Oxygen(Element):
    melting_point = -283
    boiling_point = -182


class Iron(Element):
    melting_point = -283
    boiling_point = -182


class Chlorine(Element):
    melting_point = -283
    boiling_point = -182


if __name__ == '__main__':
    my_oxygen = Oxygen()
    my_oxygen.state_of_aggregation(-1000)
    my_oxygen.state_of_aggregation(-200, 'F')
    my_oxygen.state_of_aggregation(30)
