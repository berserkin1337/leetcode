class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        for i in range(len(nums)):
            if  len(res) == 0 or  nums[i] > res[-1] :
                res.append(nums[i])
            else:
                idx = bisect_left(res,nums[i])
                res[idx] = nums[i]
        
        return len(res)