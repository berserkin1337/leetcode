class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = set()
        for num in nums:
            a.add(num)
        
        res = []
        for i in range(1,n+1):
            if i not in a:
                res.append(i)
        return res
        