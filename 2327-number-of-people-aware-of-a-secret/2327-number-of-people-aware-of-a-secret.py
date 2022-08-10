class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*n
        MOD = 10**9 + 7
        dp[0] = 1
        
        for i in range(1,n):
            for j in range(delay,forget):
                if i - j >= 0:
                    dp[i] += dp[i-j]
                    dp[i] %= MOD
        # print(dp)
        return sum(dp[-forget:]) % MOD