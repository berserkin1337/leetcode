class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        MOD = 10 ** 9 + 7
        dp = [0 for i in range(n)]
        dp[0] = 1
        for i in range(1, n) :
            dp[i] = 1
            for j in range(i-1,-1,-1):
                if s[i] != s[j] :
                    dp[i] += dp[j]
                else:
                    dp[i] -= 1
                    dp[i] += dp[j]
                    break
        
        return (sum(dp) % MOD)