class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0 :
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        res  = 0 
        for  i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 :
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        val  = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1
                        res += val
                        matrix[i][j ] = val
        
        return res