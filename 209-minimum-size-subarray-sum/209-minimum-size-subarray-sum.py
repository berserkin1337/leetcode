class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        sum , length = 0,float('inf')
        
        while r < n:
            sum += nums[r]
            r += 1
            while sum >= target:
                length = min(length,r-l)
                sum -= nums[l]
                l += 1
        
        return (0 if length == float('inf')  else length)