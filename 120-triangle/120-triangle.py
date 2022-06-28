class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp= [0]*(len(triangle))
        dp[0] = triangle[0][0]
        
        for row in range(1,len(triangle)) :
            for  i in range(len(triangle[row]) -1 ,-1,-1):
                if i < len(triangle[row-1]) and i > 0:
                    dp[i] = triangle[row][i] + min(dp[i],dp[i-1])
                elif i == 0:
                    dp[i] = triangle[row][i] + dp[i]
                else:
                    dp[i] = triangle[row][i] + dp[i-1]
        return min(dp)
        
        