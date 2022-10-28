class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        MOD = int(1e9 + 7)
        
        # @cache
        # def dp(idx):
        #     if idx >= len(s) :
        #         return 1
        #     if s[idx] == '0' :
        #         return 0 
        #     i = idx 
        #     res = 0
        #     while i < len(s) and 1  <= int(s[idx : i + 1]) <= k :
        #         res += dp(i+1)
        #         i   += 1
        #     return res
        # return dp(0) % MOD
        s.strip()
        dp = [0 for i in range(n)]
        dp += [1]
        for  i in range(n-1,-1,-1):
            if s[i] == '0':
                continue
            j = i
            while j < len(s) and 1 <= int(s[i:j+1]) <= k :
                dp[i] += dp[j+1]
                j+=1
        return dp[0] % MOD