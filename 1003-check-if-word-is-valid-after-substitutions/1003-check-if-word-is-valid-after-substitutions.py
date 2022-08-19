class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char  == 'c':
                if stack[-2:] != ['a','b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0