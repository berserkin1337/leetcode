class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreaterElement = {}
        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                nextGreaterElement[num] = stack[-1]
            else:
                nextGreaterElement[num] = -1
            stack.append(num)
        return [nextGreaterElement[num] for num in nums1]