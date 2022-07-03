class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        n = len(horizontalCuts)
        m = len(verticalCuts)
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        maxHorizontalDist = horizontalCuts[0]
        maxVerticalDist = verticalCuts[0]
        
        for i in range(n):
            maxHorizontalDist = max(horizontalCuts[i+1] - horizontalCuts[i]  , maxHorizontalDist)
            # print(horizontalCuts[i+1] , horizontalCuts[i] , i )
        
        for i in range(m):
            maxVerticalDist = max(verticalCuts[i+1]- verticalCuts[i],maxVerticalDist)
        # print(maxVerticalDist,maxHorizontalDist)
        res = (maxVerticalDist * maxHorizontalDist) % (10**9 + 7)
        return res