class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) <= 2: return '/'.join(map(str, nums))
        return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"
