class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        dic = {"[":"]","(":")","{":"}"}
        stack = []
        for char in s:
            if char in ['[',"{","("]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                opening = stack.pop()
                if opening not in dic or dic[opening] != char:
                    return False
        if len(stack):
            return False
        return True
