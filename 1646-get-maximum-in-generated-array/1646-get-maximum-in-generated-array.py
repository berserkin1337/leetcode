class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 :
            return 0
        if n == 1:
            return 1
        dp = [0 for i in range(n+1)]
        dp[0] , dp[1] = 0  , 1
        for i in range(n+1):
            if 2*i > n :
                break
            dp[2*i] = dp[i]
            if 2*i + 1 > n :
                break
            dp[2*i + 1] = dp[i] + dp[i+1]
        return max(dp)
            