class Solution:
    def isUgly(self, n: int) -> bool:
        s = set()
        if n == 0:
            return 0
        while n %2 == 0:
            s.add(2)
            n /= 2
        if n < 0:
            return False
        if n == 0:
            return 0
        for i in range(3,int(math.sqrt(n)) + 1 , 2):
            while n % i == 0:
                s.add(i)
                n /= i
        
        if n > 2:
            s.add(n)
        primes = [2,3,5]
        for num in s :
            if num not in primes:
                return False
        return True