# Задача 3. Файл-тест. Есть файл, в котором хранятся числа в следующем формате:
#
# 2 4 5;3 2
# 3 2 1;2 0
# 6 5 2 1 2;3 1
# .....
# Цифры до точки с запятой надо суммировать, потом делить на их количество.
# В первой строке сумма будет 11, разделить на их количество, т.е. на 3, получается 3 целых и в остатке 2.
# Аналогичным образом во второй строке 6 делим на три, ровно два и в сотатке ноль, в третьей строке сумма 16,
# на 5 делим, получаем 3 и 1 в остатке. Вот так:
#
# 2 4 5;3 2                 2+4+5/3 = 3, в остатке 1
# 3 2 1;2 0                 3+2+1/3 = 2, в остатке 0
# 6 5 2 1 2;3 1         6+5+2+1+2/5 = 3, в остатке 1
# .....
# Задача: проверить каждую строку файла, если строка записана верно, вывести ее и после написать True,
# если строка не верна, вывести результат с пометкой False.


def is_all_list_digits(my_list):
    return all(list(map(lambda x: x.isdigit(), my_list)))


filename = 'file_test.txt'
if __name__ == '__main__':
    f = open(filename, 'r')

    for line_number, line in enumerate(f, 1):

        split_line = line.split(';')
        nums = split_line[0].split()
        controls = split_line[1].split()

        if not is_all_list_digits(nums) or not is_all_list_digits(controls):
            print(f'wrong line {line_number} in file {filename}: "{line.strip()}"')
            continue

        nums = list(map(int, nums))
        controls = list(map(int, controls))

        print(line.strip(), sum(nums)//len(nums) == controls[0] and sum(nums) % len(nums) == controls[1])
    f.close()
