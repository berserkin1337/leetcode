class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(nums):
            last,curr = 0,0
            for num in nums:
                last,curr = curr, max(last+num,curr)
            return curr
        
        return max(rob1(nums[1:]),rob1(nums[:-1]) )