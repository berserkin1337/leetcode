class Solution:
    def numOfWays(self, n: int) -> int:
        mod = int(1e9 + 7)
        if n == 1:
            return 12
        a,b =  6 , 6
        
        for i in range(1,n):
            a,b = 2*a + 2*b,2*a+3*b
        return (a+b)%mod