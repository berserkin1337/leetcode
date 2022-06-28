class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp =[[0 for i in range(len(triangle[j]))] for j in range(len(triangle))]
        
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                # if j < len(triangle[i-1]) and j - 1 >= 0 :
                #     dp[i][j] = triangle[i][j] +  min(dp[i-1][j],dp[i-1][j-1])
                # elif j - 1 < 0:
                #     dp[i][j] = triangle[i][j] + dp[i-1][j]
                # elif j == len(triangle[i-1]):
                #     dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                dp[i][j] = triangle[i][j] + min(dp[i-1][j] if j < len(triangle[i-1]) else float('inf') , dp[i-1][j-1] if j -1 >= 0 else float('inf') ) 
        return min(dp[-1])