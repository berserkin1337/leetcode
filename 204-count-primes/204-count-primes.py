class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        sieve = [1]*(n)
        sieve[0] = 0
        sieve[1] = 0
        for i in  range(2,int(n**0.5) + 1):
            if sieve[i] == 1:
                
                num  = 2
                sieve[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)

                
        return sum(sieve)
        
        
        