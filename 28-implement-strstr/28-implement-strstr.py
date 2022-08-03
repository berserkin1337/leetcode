class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 :
            return 0
        if len(haystack) < len(needle):
            return -1
        
        n = len(needle)
        
        for i in range(len(haystack) - n +  1):
            s1 = haystack[i:i+n]
            if s1 == needle :
                return i
        return -1