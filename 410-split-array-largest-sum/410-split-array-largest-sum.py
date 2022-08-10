class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.dic = {}
        self.lookup = [0] * len(nums)
        self.lookup[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            self.lookup[i] = self.lookup[i+1] + nums[i]
        def dfs(start,k) :
            if k == 0 or start >= len(nums):
                return 0
            if k == 1:
                return self.lookup[start]
            if (start,k ) in self.dic:
                return self.dic[(start,k)]
            res = float('inf')
            curSum = 0
            for i in range(start,len(nums) - k + 1) :
                curSum += nums[i]
                if curSum > res:
                    break
                res = min(res, max(curSum,dfs(i+1,k-1)) )
            self.dic[(start,k)] = res
            return self.dic[(start,k)] 
        
        return dfs(0,m)