class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        n = len(stones)
        indices = {}
        for i,stone in enumerate(stones):
            indices[stone] = i
        
        
        dp = [[False for i in range(n + 1)] for  _ in range(n)]
        
        dp[1][1] = True
        for i in range(1,n-1):
            for j in range(1,n+1):
                if dp[i][j]:
                    if stones[i] + j in indices:
                        dp[indices[stones[i] + j]][j] = True
                    if j != 1:
                        if stones[i] + j  - 1 in indices :
                            dp[indices[stones[i]+j - 1]][j-1] = True
                    if stones[i] + j + 1 in indices:
                        dp[indices[stones[i] + j + 1]][j + 1] = True
        
        for i in range(n + 1):
            if dp[-1][i] == True:
                return True
        return False