class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = nums[::-1]
        nextGreaterElement = [0 for i in range(len(nums))]
        for i in range(len(nums) - 1, - 1,-1):
            # print(i,stack)
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                nextGreaterElement[i] = stack[-1]
            else:
                nextGreaterElement[i] = -1
            stack.append(nums[i])
        return nextGreaterElement