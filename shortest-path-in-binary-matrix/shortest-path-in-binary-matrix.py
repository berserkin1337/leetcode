class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        # I am stupid this is bfs
        q = deque()
        visited = [[False for i in range(n)] for j in range(n)]
        q.append((0,0))
        dist = [[-1 for i in range(n)] for j in range(n)]
        dx = [1,1, 1,0, 0,-1,-1,-1]
        dy = [1,0,-1,1,-1, 0, 1,-1]
        dist[0][0] = 1
        visited[0][0] = True
        while len(q) != 0 :
            (x,y) = q.popleft()
            
            for a,b in zip(dx,dy):
                u,v = x+a,y+b
                if u>=0 and u < n and v >= 0 and v <n and visited[u][v] == False and grid[u][v] == 0 :
                    q.append((u,v))
                    dist[u][v] = dist[x][y] + 1
                    visited[u][v] = True
        print(dist)
        return dist[-1][-1]