class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m = len(heights) , len(heights[0])
        max_value = max(max(x) for x in heights)
        min_value = min(min(x) for x in heights)
        high = max_value - min_value
        low  = 0
        
        def isSafe(n,m,i,j):
            return ( i>=0  and i <n and j >= 0 and j < m)
        
        def bfs(k):
            n,m = len(heights) , len(heights[0])
            queue   = deque()
            dx = [ -1, 0, 1, 0]
            dy = [ 0, 1, 0, -1]
            visited = defaultdict(bool)
            queue.append([0,0])
            while len(queue):
                
                [x,y] = queue.popleft()
                # print([x,y])
                if visited[(x,y)]:
                    continue
                visited[(x,y)] = True
                for xd,xy in zip(dx,dy):
                    
                    ex,ey = x + xd , y + xy
                    # print(ex,ey,xd,xy)
                    if isSafe(n,m,ex,ey):
                        if abs(heights[ex][ey] - heights[x][y]) <= k:
                            queue.append([ex,ey])
                # print(queue)
            if visited[(n-1,m-1)]:
                return True
            return False
        min_num = high
        # print(bfs(2))
        while low < high :
            mid = (low + high) // 2
            if bfs(mid):
                min_num = min(min_num , mid)
                high = mid
            else:
                low = mid + 1
        return min_num
        