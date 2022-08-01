from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def checkAdjacent(num):
            # print(num)
            currentlyPicking = False
            curr = 0
            total = 0
            for day in bloomDay:
                if currentlyPicking:
                    if day <=num:
                        # print(i)
                        curr +=1
                    else:
                        total +=  (curr//k)
                        curr = 0
                        currentlyPicking = False
                else:
                    if day <= num:
                        curr = 1
                        currentlyPicking = True
            total +=  (curr//k)
            # print(total)
            if total >= m :
                return True
            return False
            
        n = len(bloomDay)
        low , high = min(bloomDay) , max(bloomDay)
        found = False
        while low < high :
            mid = low + (high - low)//2
            # print(mid)
            # print(checkAdjacent(mid), mid)
            if(checkAdjacent(mid)):
                found = True
                high = mid
            else:
                low = mid + 1
        mid = low + (high - low)//2
        # print(mid)
        if(checkAdjacent(mid)):
            found = True

        return low if  found else -1
