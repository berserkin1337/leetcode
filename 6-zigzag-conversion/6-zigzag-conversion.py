class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        row  = 1
        rows = [0]*len(s)
        curr = 1
        if numRows == 1:
            return s
        for i , n in enumerate(s):
            rows[i] = row
            if curr ==  1:
                if row == numRows:
                    curr = -1
                row +=curr
                continue
            if curr == -1:
                if row == 1:
                    curr = 1
                row += curr
                continue
        res = ""
        for i in range(1,numRows+1):
            for j in range(len(s)):
                if rows[j] == i:
                    res  = res + s[j]
        
        return res
            