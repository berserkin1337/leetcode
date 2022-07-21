class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        global lookup
        lookup = {}
        def target2(i,sum):
            if (i,sum) in lookup:
                return lookup[(i,sum)]
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0

            choice1 = target2(i+1,sum+nums[i])
            choice2 = target2(i+1,sum-nums[i])
            lookup[(i,sum)] = choice1 + choice2
            return lookup[(i,sum)]
            
        
        return target2(0,0)