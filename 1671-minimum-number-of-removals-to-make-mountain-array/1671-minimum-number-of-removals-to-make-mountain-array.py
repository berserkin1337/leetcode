class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        #num( lis ending at this index )   + lds(starting at this index)
        
        @cache
        def lis(idx):
            if idx == 0:
                return 1
            res = 1
            for i in range(idx-1,-1,-1):
                if nums[i] < nums[idx] :
                    res = max(res, lis(i) + 1)
            return res
        
        
        @cache
        def lds(idx):
            if idx == len(nums) - 1:
                return 1
            res = 1
            for i in range(idx+1,len(nums)):
                if nums[idx] > nums[i]:
                    res = max(res, lds(i) + 1)
            return res
        res  = float('inf')
        for i in range(1,len(nums) - 1):
            if lis(i) == 1 or lds(i) ==1:
                continue
            res = min(res, len(nums) - lis(i) - lds(i) +  1 )
            # print(res)
        return res