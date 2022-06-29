class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        stack = []
        for i,num in enumerate(nums):
            # print(i)
            if not stack  or nums[stack[-1]] > num:
                stack.append(i)
        
        res = 0
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                res = max(res,i-stack.pop())
        
        return res
            