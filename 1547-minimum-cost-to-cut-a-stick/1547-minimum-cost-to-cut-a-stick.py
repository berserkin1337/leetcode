class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.sort()
        
        @cache
        def dp(i,j):
            res = float('inf')
            for x in cuts:
                if  i<x<j:
                    curr = j - i  +  dp(i,x) + dp(x,j)
                    res = min(res, curr)
                    # if i == 0 and j == n:
                    #     print(x,curr)
            return res if res != float('inf') else 0
        return dp(0,n)