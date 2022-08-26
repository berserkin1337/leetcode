class Solution:
    
    
    def maxCoins(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        nums = [1] + nums + [1]
        
        @cache
        def dfs(i,j):
            
            res = 0
            for k in range(i+1,j):
                res = max(res, nums[i]*nums[k]*nums[j] + dfs(i,k) + dfs(k,j))
            # print(res)
            return res
        return dfs(0,len(nums)-1)