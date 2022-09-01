class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        
        
        @cache
        def dfs(i,j):
            if j <=i:
                return 0
            
            res = float('inf')
            for cut in cuts:
                if cut > i and cut < j :
                    res = min(res,  dfs(i,cut) + dfs(cut,j) + j -  i )
            return res if res != float('inf') else 0
        return dfs(0,n)