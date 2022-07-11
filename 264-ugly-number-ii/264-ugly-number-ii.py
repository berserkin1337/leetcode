class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp  =  [1]*(n)
        pos_2 = 0
        pos_3 = 0
        pos_5 = 0
        dp[0] = 1
        for i in range(1,n):
            s2,s3,s5 = dp[pos_2]*2,dp[pos_3]*3,dp[pos_5]*5
            s = min(s5,s2,s3)
            if  s == s2:
                pos_2 += 1
            if s == s3:
                pos_3 += 1
            if s == s5:
                pos_5 += 1
            dp[i] = s
        return dp[-1]        