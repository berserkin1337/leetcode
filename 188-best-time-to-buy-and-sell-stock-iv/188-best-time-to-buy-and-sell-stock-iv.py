class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        
        dp = [[0 for i in range(len(prices) )] for _ in range(k+1) ]
        for i in range(1,k+1):
            temp = -prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1],prices[j] + temp)
                temp = max(temp , -prices[j] + dp[i-1][j-1])
                
        return dp[k][-1]