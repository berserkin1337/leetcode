class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        mat = [["" for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = encodedText[i*cols + j]
        # print(mat)
        
        i = 0 
        j = 0
        
        s = ""
        while i < rows and j < cols :
            jj = j
            
            while i < rows and jj < cols :
                s += mat[i][jj]
                i += 1
                jj += 1
        
            j += 1
            i = 0
        
        return s.rstrip()