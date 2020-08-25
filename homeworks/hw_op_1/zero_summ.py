# 6. Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.


class Triples:
    def find_triplets(self, arr):
        result = []
        list_set = set(arr)
        len_list = len(list_set)
        for i in range(len_list - 1):
            for j in range(i + 1, len_list):
                for k in range(j + 1, len_list):
                    l = [arr[i], arr[j], arr[k]]
                    if not sum(l):
                        result.append(l)
        return result


arr1 = [0, -1, 2, -3, 1]
print(Triples().find_triplets(arr1))
