class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[i] is the stock the last stock bought
        maxxIdx = {}
        dp = [0 for i in range(n)]
        maxxIdx[0] = 0 
        k  =  -prices[0] - fee + maxxIdx[0]
        for i in range(1,n):
            # print(k)
            dp[i] = max(dp[i],prices[i] + k)
            maxxIdx[i] = max(maxxIdx[i-1] , dp[i])
            k = max(k, -prices[i] - fee + maxxIdx[i] )
        # print(dp)
        return max(dp)