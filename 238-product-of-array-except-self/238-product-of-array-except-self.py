class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        for i in range(n):
            res[i] =  1 if i==0 else nums[i-1]*res[i-1]
        suffix = 1
        
        for  i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix*=nums[i]
        
        return res
        
        