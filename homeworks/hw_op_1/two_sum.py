class TwoSum:
    @staticmethod
    def get_sum_indexes(target, num_list):
        for i in num_list:
            if target - i in num_list:
                return num_list.index(i), num_list.index(target - i)


trgt = 85
lst = [3, 4, 6, 0, 5, 20, 50, 25, 45, 40, 70]
i1, i2 = TwoSum().get_sum_indexes(trgt, lst)
print(f"index1 = {i1}, index2 = {i2}")
