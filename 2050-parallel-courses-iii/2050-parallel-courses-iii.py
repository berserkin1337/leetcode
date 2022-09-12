class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        inDegree = [0 for i in range(n+1)]
        for [prevCourse,nextCourse] in relations :
            adj[prevCourse].append(nextCourse)
            inDegree[nextCourse] += 1
    
        dist=  [0 for i in range(n + 1)]
        queue = deque()
        for i in range(1,len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
                dist[i] = time[i-1]
        while len(queue):
            u = queue.popleft()
            for v in adj[u]:
                inDegree[v] -= 1
                dist[v] = max(dist[v] , dist[u] + time[v-1])
                if inDegree[v] == 0:
                    queue.append(v)
        return max(dist)