class Solution:
    def isPalindrome(self, s: str) -> bool:
        def strip(s):
            ans = ""
            for i in s:
                if i.isalnum():
                    ans += i.lower()
            return ans
        newString = strip(s)
        return newString == newString[::-1]