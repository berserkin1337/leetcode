class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        dp = [0]*len(days)
        days.sort()
        
        dp[0] = min(costs)
        
        for i in range(1,n):
            dp[i] = dp[i-1] + min(costs)
            j = i-1
            while j >= 0 and days[i] - days[j] <=6:
                # print(j)
                j -= 1
            dp[i] = min(( dp[j] if j >= 0 else 0)  + costs[1], dp[i])
            j = i-1
            while j >= 0 and days[i] - days[j] <= 29:
                j -= 1
            dp[i] = min(dp[i],(  dp[j]  if j >= 0 else 0)+ costs[2])
        
        print(dp)
        return dp[-1]