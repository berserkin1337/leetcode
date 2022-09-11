class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        t,n = len(rooms) - 1,len(rooms)
        visited = [False for i in range(n)]
        queue = deque()
        queue.append(0)
        while len(queue) :
            room = queue.popleft()
            if visited[room]:
                continue
            visited[room] = True
            for dest in  rooms[room]:
                queue.append(dest)
        return False if any(i==False for i in visited) else True