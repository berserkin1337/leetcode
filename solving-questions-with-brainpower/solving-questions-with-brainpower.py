class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0 for i in range(n)]
        for i in range(n-1,-1,-1):
            dp[i] = questions[i][0]
            if i + questions[i][1] + 1 < n :
                dp[i] += dp[i+questions[i][1] + 1]
            if i + 1 < n :
                dp[i] = max(dp[i],dp[i+1])
        return max(dp) 