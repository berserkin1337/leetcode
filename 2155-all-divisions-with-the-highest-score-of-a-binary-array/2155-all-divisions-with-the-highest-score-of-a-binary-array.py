class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n =len(nums)
        p0l = [0 for i in range(n)]
        p1l = [0 for i in range(n)]
        p0l[0] = 0 if nums[0] == 1 else 1
        p1l[-1] = nums[-1]
        for i in range(1,n):
            p0l[i] = p0l[i-1]
            p0l[i] +=  ( 1 if nums[i] == 0 else 0)
        p0l = [0] + p0l
        for i in range(n-2,-1,-1):
            p1l[i] = p1l[i+1]
            p1l[i] += nums[i]
        p1l.append(0)
        maxVal = max(left + right for left,right in zip(p0l,p1l))
        res = []
        for i in range(0,n+1):
            if p0l[i] + p1l[i] == maxVal:
                res.append(i)
        return res