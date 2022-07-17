class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        MOD = 10**9 + 7
        dp = [[0 for i in range(10) ] for j in range(n)]    
        for i in range(10):
            dp[0][i] = 1
        for i in range(1,n):
            dp[i][0] = dp[i-1][4] + dp[i-1][6]
            dp[i][1] = dp[i-1][6] + dp[i-1][8]
            dp[i][2] = dp[i-1][7] + dp[i-1][9]
            dp[i][3] = dp[i-1][4] + dp[i-1][8]
            dp[i][4] = dp[i-1][9] + dp[i-1][3] + dp[i-1][0]
            dp[i][5] = 0
            dp[i][6] = dp[i-1][7] + dp[i-1][1] + dp[i-1][0]
            dp[i][7] =dp[i-1][6] + dp[i-1][2]
            dp[i][8] = dp[i-1][1] + dp[i-1][3]
            dp[i][9] = dp[i-1][4] + dp[i-1][2]
        
        return sum(dp[-1])%MOD