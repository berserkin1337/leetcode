class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.res = 0    
        global lookup
        lookup = set()
        def target2(i,sum):
            if (i,sum) in lookup:
                return False
            if i == len(nums):
                if sum == target:
                    self.res += 1
                    return True
                else:
                    lookup.add((i,sum))
                    return False

            choice1 = target2(i+1,sum+nums[i])
            choice2 = target2(i+1,sum-nums[i])
            if choice1== False and choice2==False:
                lookup.add((i,sum))
                return False
            return True
        target2(0,0)
        return self.res
