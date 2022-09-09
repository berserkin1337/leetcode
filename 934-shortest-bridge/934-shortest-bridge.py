class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dxx = [0,0,1,-1]
        dyy = [1,-1,0,0]
        self.queue = []
        def mark2(i,j):
            dxx = [0,0,1,-1]
            dyy = [1,-1,0,0]
            # print(i,j , grid[i][j])
            
            grid[i][j] = 2
            self.queue.append((i,j))
            
            for dx,dy in zip(dxx,dyy):
                
                x,y = i + dx , j + dy
                # print(x,y, i,j)
                if 0 <= x < len(grid) and  0<= y < len(grid) and grid[x][y] == 1:
                    mark2(x,y)
                
        marked = False
        start = None
        step = 0
        for i in range(n):
            if marked:
                break
            for j in range(n):
                if marked :
                    break
                if grid[i][j] == 1:
                    mark2(i,j)
                    marked = True
                    start = (i,j)
        
        step = 0
        print(grid)
        
        while len(self.queue) :
            newQ = []
            
            for (i,j) in self.queue:
                for (dx,dy ) in zip(dxx,dyy):
                    x,y = i+ dx,j +dy
                    
                    if 0<=x<n and 0<=y<n and grid[x][y] != 2:
                        if grid[x][y] == 1:
                            return step
                        grid[x][y] = 2
                        newQ.append((x,y))
            self.queue = newQ
            step += 1
        # print(grid)
        return -1
            
            