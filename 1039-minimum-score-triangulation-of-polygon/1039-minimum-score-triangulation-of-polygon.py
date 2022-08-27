class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @cache
        def dfs(i,j):
            if j - i == 2:
                return values[i]*values[i+1]*values[j]
            if j - i <2:
                return 0
            res = float('inf')
            for k in range(i+1,j):
                res = min(res , values[i]*values[k]*values[j] + dfs(i,k) + dfs(k,j))
            return res
        return dfs(0,len(values) - 1)