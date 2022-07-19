class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1,1])
        if numRows == 2:
            return res
        for i in range(2,numRows):
            curr = [1]
            for j in range(1,i):
                curr.append(res[-1][j]+res[-1][j-1])
            curr.append(1)
            res.append(curr)
        return res
        
        