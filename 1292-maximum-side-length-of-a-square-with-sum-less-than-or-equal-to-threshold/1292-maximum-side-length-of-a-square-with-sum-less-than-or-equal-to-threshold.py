from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        self.subMatrixSum = [[0 for i in range(n)] for j in range(m)]

        def enough(side):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i >= side - 1 and j >= side - 1:
                        sumOfSquare = self.subMatrixSum[i][j]
                        if i >= side:
                            sumOfSquare -= self.subMatrixSum[i-side][j]
                        if j >= side:
                            sumOfSquare -= self.subMatrixSum[i][j-side]
                        if i >= side and j >= side:
                            sumOfSquare += self.subMatrixSum[i-side][j-side]
                        if sumOfSquare <= threshold:
                            return True
            return False

        self.subMatrixSum[0][0] = mat[0][0]
        for i in range(1, m):
            self.subMatrixSum[i][0] = self.subMatrixSum[i-1][0] + mat[i][0]
        for i in range(1, n):
            self.subMatrixSum[0][i] = self.subMatrixSum[0][i-1] + mat[0][i]
        for i in range(1, m):
            for j in range(1, n):
                self.subMatrixSum[i][j] = self.subMatrixSum[i-1][j] + \
                    self.subMatrixSum[i][j-1] + mat[i][j] - \
                    self.subMatrixSum[i-1][j-1]
        low, high = 0, min(m, n)
        res = 0
        while low <= high:
            mid = low + (high - low) // 2
            if mid == 0:
                res = 0
                break
            if enough(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res