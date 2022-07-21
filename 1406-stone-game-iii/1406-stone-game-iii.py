class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        if len(stoneValue)  == 0:
            return "Tie"
        dp =  [0]*(len(stoneValue) + 1)
        n = len(stoneValue)
        for i in range(len(stoneValue)-1,-1,-1):
            dp[i] = -float('inf')
            take = 0
            for k in range(3):
                if k + i >= n :
                    break
                take += stoneValue[i+k]
                dp[i] = max(dp[i],take - (dp[i+k+1] if (i + k + 1) <  n else 0))
        # print(dp)
        if dp[0]  < 0:
            return "Bob"
        if dp[0] > 0 :
            return "Alice"
        return "Tie"
