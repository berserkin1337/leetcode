class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)        
        dic = {}
        dp = [1]*n
        
        dp[0] = 1
        dic[arr[0]] = 0
        for i in range(1,n):
            if (arr[i]-difference)  in dic:
                dp[i] = dp[dic[arr[i]-difference]] + 1
            dic[arr[i]]  = i
        # print(dp) 
        return max(dp)
