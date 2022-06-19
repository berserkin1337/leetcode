class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        b = set(arr)
        nums = sorted(list(b))
        MOD  = int(1e9 + 7)
        n = len(nums)
        dp = [1]*(n)
        for i,num in enumerate(nums):
            for j in range(i):
                if num % nums[j] == 0 and num//nums[j] in b:
                    dp[i]+= (dp[j] * dp[nums.index(num//nums[j])])%MOD
        # print(b)
        # print(dp)
        return sum(dp)%MOD