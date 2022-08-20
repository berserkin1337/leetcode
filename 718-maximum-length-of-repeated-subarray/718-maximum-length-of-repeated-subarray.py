class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        dp = [[0 for i in range(m)] for j in range(n)]
        
        #dp[i][j] = max length of a repeated subarray that ends at pos i in first array , pos j in second array
        
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j] :
                    dp[i][j] = 1 + (dp[i-1][j-1] if (i > 0 and j >0 ) else 0 )
        return max(map(max, dp))  
            