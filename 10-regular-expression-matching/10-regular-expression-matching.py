class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s)+1)]
        dp[0][0] =  True
        for j in range(1,len(p)+1):
            if p[j-1] == '*' :
                dp[0][j] = dp[0][j-2]
        
        
        for i in range(1,len(s)+1):
            for j in range(1,len(p) + 1):
                if p[j-1] in {s[i-1] , '.'} :
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
        # print(dp)
        return dp[-1][-1]