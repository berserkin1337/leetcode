class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [0 for i in range(len(nums))]
        for i in range(len(nums) - 1 , - 1 ,-1):
            cur = 0
            while len(stack ) and  stack[-1] < nums[i]:
                cur += 1
                stack.pop()
            res[i] = cur
            res[i] += 1 if len(stack) is not 0 else 0
            stack.append(nums[i])
        return res