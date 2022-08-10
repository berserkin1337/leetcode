class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        #check if there is a subset in the array which sums to totalSum//2
        dp = [[False for i in range(totalSum + 1 ) ] for j in range(n)]
        dp[0][0] = True
        dp[0][nums[0]] = True
        ans = False
        
        for i in range(1, len(nums)):
            dp[i][:] = dp[i-1][:]
            
            for j in range((totalSum) + 1) :
                if j + nums[i] <= totalSum:
                    dp[i][j+nums[i]] |= dp[i-1][j]
                    
            if dp[i][totalSum//2] == True :
                ans = True
                break
        
        return ans