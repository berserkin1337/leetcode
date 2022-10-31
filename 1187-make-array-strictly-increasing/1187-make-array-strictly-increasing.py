from bisect import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        
        
        @cache
        def dp(idx,prevVal):
            if idx == len(arr1) :
                return 0
            res1 = float('inf')
            if arr1[idx]  > prevVal :
                res1 =  dp(idx + 1 , arr1[idx])
            res2  = float('inf')
            index = bisect(arr2,prevVal)
            if index != len(arr2) :
                res2 = dp(idx + 1,  arr2[index]) + 1
            return min(res1,res2)
        
        return -1 if dp(0,-float('inf')) ==  float('inf') else dp(0,-float('inf'))