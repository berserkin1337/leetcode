class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if s == "abc":
            return True
        a = -1
        for i in range(len(s)-2):
            if s[i:i+3] == "abc":
                a = i
                break
        if a == -1:
            return False
        return self.isValid(s[:i] + s[i+3:])