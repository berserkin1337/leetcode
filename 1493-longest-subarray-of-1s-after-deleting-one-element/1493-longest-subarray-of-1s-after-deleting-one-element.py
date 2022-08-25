class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        if sum(nums) == len(nums): return len(nums) - 1

        n = len(nums)
        dp = [[0,0] for i in range(n)]
        dp[0][0] = nums[0]
        for i in range(1,n):
            if nums[i] == 1:
                dp[i][0] , dp[i][1] = dp[i-1][0] + 1 , dp[i-1][1]  + 1
            else:
                dp[i][0] , dp[i][1] = 0 , dp[i-1][0]
        # print(dp)
        return max([i for j in dp for i in j])  
