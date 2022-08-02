class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len( matrix )
        # isFeasible() checks that the number of elements greater than mid in the array are
        # greater than or equal to  k so our goal is to find the min element for which               isFeasible(k) is satisfied 
        def isFeasible(mid):
            curr = 0
            for i in range(len(matrix)):
                j = 0
                while j < n and  matrix[i][j]  <= mid   :
                    j+=1
                curr += j
            if curr >= k:
                return True
            return False
        low ,high = matrix[0][0] , matrix[-1][-1]
        res = -1
        while (low<=high):
            mid = low + (high - low)//2
            
            if isFeasible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res