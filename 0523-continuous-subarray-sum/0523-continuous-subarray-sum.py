class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0 for i in range(len(nums))]
        prefix[0] = (nums[0])%k
        n = len(nums)
        x = set()
        x.add(0)
        for i in range(1,n):
            prefix[i] = (prefix[i-1] + nums[i])  % k
            if prefix[i] in x :
                return True
            
            x.add(prefix[i-1])
        return False
        
