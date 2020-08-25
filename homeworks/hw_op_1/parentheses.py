# 3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].'
# ' These brackets must be close in the correct order, for example "()" and "()[]{}" are valid '
# but "[)", "({[)]" and ' '"{{{" are invalid.

class Parentheses:
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    def is_parentheses(self, string):
        stack = []
        for i in string:
            if i in self.open_list:
                stack.append(i)
            if i in self.close_list:
                if self.close_list.index(i) == self.open_list.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


balanced_string = '123 (14) [2, 3: {16, 9}, (90, a[1])]'
unbalanced_string = '44 (5t6y) [2, 3: {16, 9}, {(90, a[1]))]'

print(Parentheses().is_parentheses(balanced_string))  # True
print(Parentheses().is_parentheses(unbalanced_string))  # False
print(Parentheses().is_parentheses('{}'))   # True
print(Parentheses().is_parentheses('{'))  # False
