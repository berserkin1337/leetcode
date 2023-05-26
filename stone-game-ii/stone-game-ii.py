class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def dp(p,m,idx):
            if idx>=n:
                return 0
            res = int(1e9) if p == 1 else -1
            s = 0
            for i in range(idx,min(idx  + 2*m,n)) :
                s += piles[i]
                if p == 0 :
                    res = max(res, s + dp(1,max(m,i-idx+1),i+1))
                else :
                    res = min(res,dp(0,max(m,i-idx+1),i+1))
            return res
        return dp(0,1,0)