class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        rmax = [0] * (len(nums))
        rmax[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            rmax[i] = max(nums[i],rmax[i+1])
        
        left , right = 0, 0 
        res = 0
        while right < len(nums) :
            
            while left < right and nums[left]  > rmax[right] :
                left += 1
            res = max(res,right - left)
            right += 1
        return res
        