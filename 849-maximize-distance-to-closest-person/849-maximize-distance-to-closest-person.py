class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        lFix = [0]*n
        rFix = [0]*n
        curr = 1 if  seats[0] == 0 else 0 
        lFix[0] = float('inf')
        rFix[-1] = float('inf')
        for i in range(1,n):
            if seats[i] == 1:
                curr = 0
            else:
                lFix[i] = curr
                curr += 1
        curr = 1 if seats[-1] == 0 else 0
        for i in range(n-2,-1,-1):
            if seats[i] == 1:
                curr = 0
            else:
                rFix[i] = curr
                curr += 1
        res = float(-inf)
        for i in range(n):
            maxDist  = min(lFix[i] , rFix[i])
            res = max(res, maxDist)
        # print(lFix, rFix)
        return res + 1