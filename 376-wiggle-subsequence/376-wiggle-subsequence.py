class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [1]*(n)
        down = [1]*(n)
        up[0],down[0] = 1,1
        
        for i in range(1,n):
            for j  in range(i):
                if nums[j] > nums[i]:
                    down[i] = max(down[i],1+up[j])
                elif nums[j]<nums[i]:
                    up[i] = max(up[i],1+down[j])
        return  max(max(up),max(down))