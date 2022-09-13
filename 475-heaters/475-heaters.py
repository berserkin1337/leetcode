class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n,m = len(houses) , len(heaters)
        houses.sort()
        heaters.sort()
        def check(houses,r,heaters):
            arr = [False for i in range(len(houses))]
            i , j  = 0 , 0
            while j < len(heaters) and i < len(houses):
                if  heaters[j]  - r <=houses[i] <=  heaters[j] + r :
                    if i == len(houses) - 1:
                        i += 1
                    while i < len(houses) and houses[i] <= heaters[j] + r :
                        i += 1
                    
                    j += 1
                elif  houses[i] > heaters[j] + r:
                    j += 1
                else:
                    break
            return i >= len(houses)
        # print(check(houses,1,heaters))
        high , lo = max(max(houses), max(heaters)) , 0
        res = float('inf')
        while lo <=  high :
            mid = (lo + high) // 2
            if check(houses,mid,heaters):
                high = mid - 1
                res = min(res, mid)
            else:
                lo = mid + 1
        return res
        
                
            