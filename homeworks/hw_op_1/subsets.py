# 4. Write a Python class to get all possible unique subsets from a set of distinct integers. -


class SubSets:
    @staticmethod
    def subsets(arr):
        result = []
        for i in range(2 ** len(arr)):
            subs = [arr[j] for j in range(len(arr)) if not i & (2**j)]
            result.append(subs)
        return result

    def sub_sets(self, s_set):
        return self.subsets_recur([], s_set)

    def subsets_recur(self, current, s_set):
        if s_set:
            return self.subsets_recur(current, s_set[1:]) + self.subsets_recur(current + [s_set[0]], s_set[1:])
        return [current]


d = [1, 2, 3, 5]
print(SubSets().subsets(d))
print(SubSets().sub_sets(d))
