class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[] for  _ in range(n)]
        dp[0] = [nums[0]]
        
        for i in range(1,n):
            dp[i] = [nums[i]]
            # print(dp[i])
            for j in range(i-1,-1,-1):
                # print(j)
                if nums[i] % nums[j]  == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = list(dp[j])
                        dp[i].append(nums[i])
            # print(dp[i])
        # print(dp)
        curr = []
        for  i in range(len(dp)):
            if len(dp[i]) > len(curr):
                curr = dp[i]
        
        return curr