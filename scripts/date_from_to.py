import datetime


def dateInput():
    """Returns an instance of the class datetime.date"""
    while True:
        try:

            list_date = list(map(int, input('input date format YYYY-MM-DD :').split('-')))
            return datetime.date(list_date[0], list_date[1], list_date[2])

        except ValueError as er:
            print('ERROR :', er)

        except IndexError as er:
            print('ERROR : enter three values -', er)


date1 = dateInput()
date2 = dateInput()
# Сheck if the first date is greater than the second
if date1 > date2:
    date1, date2 = date2, date1
# Set the time period for displaying dates
delta = datetime.timedelta(days=1)

while date1 <= date2:
    print(date1)
    date1 += delta

input('Press ENTER to exit')