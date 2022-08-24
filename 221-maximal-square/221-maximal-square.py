class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r , c = len(matrix),len(matrix[0])
        dp = [[0 for i in range(c)] for j in range(r)]
        ans = 0
        for i in range(r):
            dp[i][0] =( 1 if matrix[i][0] is '1' else 0)
            ans = max(ans, dp[i][0])
        for i in range(c):
            dp[0][i] = (1 if matrix[0][i] is '1' else 0)
            ans = max(ans,dp[0][i])
        
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = 1
                ans = max(ans , dp[i][j]*dp[i][j])

                
                dp[i][j] = min(dp[i-1][j] , dp[i][j-1], dp[i-1][j-1]) + 1
                
                ans = max(ans , dp[i][j]*dp[i][j])
        # print(matrix[0][1])
        print(dp)
        return ans
        
        