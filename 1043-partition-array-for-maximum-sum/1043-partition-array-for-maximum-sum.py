class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        """
        arr = [1,15,7,9,2,5,10], k = 3
        dp[0] = 1
        dp[1] = 15*len(partitin) = 30
        dp[2] =  15*3 = 45
        dp[3] = 45 + 9 = 54
        dp[4]
        """
        dp = [0]*n
        dp[0] = arr[0]
        for i in range(1,n):
            dp[i]= dp[i-1] + arr[i]
            j = i - 1
            curLen = 1
            curMax = arr[i]
            if k != 1 :
                while j >= 0 :
                    curLen += 1
                    if curLen > k:
                        break
                    curMax = max(curMax,arr[j])
                    j-=1
                    if j < 0:
                        break
                    dp[i] = max(dp[j] + curMax*curLen,dp[i])
                if j < 0:
                    dp[i] = max(curMax*curLen,dp[i])
        # print(dp)
        return dp[-1]
