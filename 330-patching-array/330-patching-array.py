class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 1
        i = 0
        n_patch = 0
        while ans <= n:
            # print(i)
            if i < len(nums) and nums[i] <= ans:
                ans += nums[i]
                i+=1
                
            else:
                ans += ans
                n_patch +=1
        
        return n_patch