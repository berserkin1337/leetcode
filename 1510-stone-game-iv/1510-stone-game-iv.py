class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        dp[0] = False
        dp[1] = True
        for i in range(2,n+1):
            j = 1
            while  j*j <= i:
                if dp[i - j*j] == False:
                    dp[i] = True
                    break
                if i == j*j:
                    dp[i] = True
                    break
                j += 1
        print(dp)
        return dp[n]
