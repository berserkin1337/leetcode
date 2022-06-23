class Solution:
    def minDifficulty(self, nums: List[int], d: int) -> int:
        if len(nums) < d:
            return -1
        n = len(nums)
        dp = [[float('inf') for _ in range(d)] for x in range(n)]
        currMax = 0
        for i in range(n):
            currMax = max(nums[i],currMax)
            dp[i][0] = currMax
        if d == 1:
            return dp[-1][-1]
        
        for i in range(1,n):
            for j in range(1,d):
                if j > i:
                    break
                curr_max = nums[i]
                for k in range(i-1,j-2,-1):
                    curr_max = max(curr_max,nums[k+1])
                    dp[i][j]  = min(dp[i][j], dp[k][j-1] + curr_max)
        return dp[-1][-1]
                
        
        