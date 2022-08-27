class Solution:
    @cache
    def getMoneyAmount(self, n: int,add=0) -> int:
        if n<=1:
            return 0
        res = float('inf')
        for i in range(1,n+1):
            
            ans =  min(res, max(self.getMoneyAmount(i-1,add)  + i  + add ,self.getMoneyAmount(n-i,add + i) + i  + add ) ) 
            res = ans
            
        return res
    