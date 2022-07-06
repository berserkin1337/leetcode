class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        n = len(citations)
        l , h = 0 , len(citations)  -  1
        
        while l <= h:
            mid = (l+h)//2
            if mid + citations[mid] >= n:
                h = mid -1
            else:
                l = mid + 1
        return n - l