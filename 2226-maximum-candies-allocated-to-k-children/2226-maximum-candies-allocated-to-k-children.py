class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        if sum(candies) < k :
            return 0
        high = sum(candies) // k
        low = 1
        
        def isValid(num):
            total  = 0
            for i in range(len(candies)):
                total += floor(candies[i]/num)
            return total >= k
        ans=  0
        while low < high :
            mid = (low + high) // 2
            if isValid(mid):
                low=  mid + 1
                ans = max(ans, mid)
            else:
                high = mid - 1
        mid = (low + high) // 2
        if isValid(mid):
            ans = max(ans,mid)
        return ans 