class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        posi1 = any(i > 0 for i in nums1)
        posi2 = any(i>0 for i in nums2)
        if (posi1 and not posi2) :
            return min(nums1) * max(nums2)
        elif  not posi1 and posi2:
            return min(nums2) * max(nums1) 
        @cache
        def dp(i,j):
            if i < 0 or j < 0:
                return 0
            if nums1[i] * nums2[j] > 0:
                return max(dp(i-1,j-1) + nums1[i] * nums2[j], dp(i-1,j),dp(i,j-1))
            else:
                return max(dp(i-1,j),dp(i,j-1))
        return dp(len(nums1)-1,len(nums2) - 1 )