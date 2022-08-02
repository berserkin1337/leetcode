class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n  < 0:
            return False
        from math import log2
        s  = log2(n)
        if s % 1 == 0:
            return True
        return False