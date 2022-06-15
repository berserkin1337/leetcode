class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones , zeros, twos = 0,0,0
        for num in nums:
            if num == 1:
                ones +=1
            elif num == 2:
                twos +=2
            else:
                zeros += 1
        n = len(nums)
        for i in range(zeros):
            nums[i] = 0
        for i in range(zeros,zeros+ones):
            nums[i] = 1
        for i in range(zeros+ones,n):
            nums[i] = 2
        
            