class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        
        dp = [1,0,1]
        
        for num in obstacles :
            if num > 0 :
                dp[num - 1] = float('inf')
            for i in range(3):
                if i + 1 != num:
                    dp[i] = min(dp[i],dp[(i+1) % 3] + 1, dp[(i+2)%3] + 1)
        # print(dp)
        return min(dp)