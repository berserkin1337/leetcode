class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return int("01"[k-1])
        parent = self.kthGrammar(n-1,ceil(k/2))
        if parent == 0:
            if k % 2 == 0:
                return 1
            else:
                return 0
        else:
            if k % 2 == 0:
                return 0
            else:
                return 1
        
        