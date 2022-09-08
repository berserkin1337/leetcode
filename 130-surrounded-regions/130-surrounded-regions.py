class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(x,y):
            if board[x][y] != 'O':
                return 
            board[x][y] = 'V'
            dxx = [0,0,1,-1]
            dyy = [1,-1,0,0]
            
            for dx,dy in zip(dxx,dyy):
                i,j = x + dx , y + dy
                if i < len(board)  and i>=0 and j >= 0 and j < len(board[0]):
                    dfs(i,j)
        n,m = len(board) , len(board[0])
        
        for i in range(n):
            for j in {0,m-1}:
                if board[i][j] == 'O':
                    dfs(i,j)
        for i in {0,n-1}:
            for j in range(m):
                if board[i][j] == 'O':
                    dfs(i,j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        