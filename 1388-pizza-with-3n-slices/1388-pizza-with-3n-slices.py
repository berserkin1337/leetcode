class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        k = len(slices)//3
        
        def ans(num,k):
            n = len(num) 
            dp = [[0 for _ in range(k+1)] for j in range(len(num) + 1)]
            # print(dp)
            for i in range(1,n+1):
                for j in range(1,k+1):
                    if i == 1:
                        dp[i][j] = num[0]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i-2][j-1]+num[i-1])
            
            return dp[n][k]
        
        return max(ans(slices[:len(slices)-1],k),ans(slices[1:],k))