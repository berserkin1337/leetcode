class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=  len(nums)
        dic = {}
        ans = -float('inf')
        for i in range(n):
            
            for j in range(i):
                if (j,nums[i] - nums[j]) in dic:
                    dic[(i,nums[i] - nums[j])] = dic[(j,nums[i] - nums[j])] + 1
                    ans = max(ans,dic[(j,nums[i] - nums[j])] + 1)
                else:
                    dic[(i,nums[i] - nums[j])] = 2
                    ans = max(ans,2)
        return ans