class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n,m = len(nums1) , len(nums2)
        heap = []
        res = []
        heapq.heappush(heap , (nums1[0]+nums2[0],(0,0))  )
        lookup = set([(0,0)])
        while len(heap) and len(res) < k :
            (a,( b,c)) =  heapq.heappop(heap)
            
            res.append((nums1[b],nums2[c]))
            if  b < n  and c+1 < m  and (b,c+1) not in lookup:
                lookup.add((b,c+1))
                heapq.heappush(heap,(nums1[b]+nums2[c+1],(b,c+1)))
                
            if b+1 < n and  (b+1,0) not in lookup  :
                lookup.add((b+1,0))
                heapq.heappush(heap,(nums1[b+1]+nums2[0],(b+1,0)))
        
        return res