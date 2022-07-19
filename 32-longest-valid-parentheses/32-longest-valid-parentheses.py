class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if len(s) == 0 or len(s)==1:
            return 0
        n = len(s)
        maxSize = 0
        longest = [0]*n
        for i in range(1,n):
            if s[i] == ')':
                if s[i-1] == '(':
                    longest[i] = longest[i-2] + 2 if i-2 >= 0 else 2
                else:
                    if (i - longest[i-1] - 1>=0) and s[i-longest[i-1]-1] == '(' :
                        longest[i] = longest[i-1] + 2 + (longest[i-longest[i-1]-2] if (i-longest[i-1]-2 >= 0) else 0)
        return max(longest)
