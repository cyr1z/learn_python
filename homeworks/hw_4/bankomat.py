# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры


def get_digit(welcome_string='Enter the number: '):
    line = ''
    while not line.isdigit():
        line = input(welcome_string)
    return int(line)


nominals = [1000, 500, 200, 100, 50, 20, 10, 5, 2]

if __name__ == '__main__':
    number = get_digit()

    # # from big to small nominals
    # nominals.sort(reverse=True)
    # for i in nominals:
    #     if number//i:
    #         print(f'{number//i} Ã— {i}')
    #         number %= i

    nominals.sort()
    cash = {}   #
    max_bill_count = 10
    max_amount = sum([x * 10 for x in nominals])

    if number % nominals[0] and nominals[0] != 2:   # we can`t cash out 12, if we don`t have a "2" nominal
        print(f"enter the amount of multiple {nominals[0]} please")
        exit()

    if number < nominals[0]:    # we can't cash out "2" if minimal nominal is "5"
        print(f"enter bigger number please. Minimal is {nominals[0]} ")
        exit()

    for idx, nominal in enumerate(nominals):
        if not number:  # check if there is a residue
            break

        if idx == len(nominals) - 1:                # last nominal cash out all residue
            if number // nominal > max_bill_count:  # but not bigger 10
                cash = {}
                print(f"Please enter a lower or another amount. {max_amount} is maximum.")
                break
            cash[nominal] = number // nominal
            break

        # add maximum number of currency notes, without residue of division by the next nominal
        for i in range(max_bill_count, 0, -1):
            if (number - nominal * i) < 0:
                continue
            if not (number - nominal * i) % nominals[idx + 1]:
                cash[nominal] = i
                number -= nominal * i
                break

    if cash:
        check_sum = sum([i * cash[i] for i in cash])
        cash_string = ' + '.join([str(n) + 'Ã—' + str(cash[n]) for n in cash])
        print(cash_string, check_sum, sep=' = ')
