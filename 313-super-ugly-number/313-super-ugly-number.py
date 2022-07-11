class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1]*(n)
        pos = [0]*(len(primes))
        i = 1
        dic = set()
        
        while i < n:
            s = float('inf')
            min_pos  = -1
            for j in range(len(pos)):
                if s >  primes[j]*dp[pos[j]]:
                    s = primes[j]*dp[pos[j]]
                    min_pos = j
            pos[min_pos] += 1
            if s in dic:
                continue
            dp[i] = s
            dic.add(s)
            i += 1
        return dp[-1]