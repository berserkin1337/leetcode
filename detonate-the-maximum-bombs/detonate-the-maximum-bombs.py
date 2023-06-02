class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Union Find 

        n = len(bombs)
        self.edges = defaultdict(list)
        self.visited = [0 for i in range(n)]
        def maxDfs(i):
            if self.visited[i] :
                return 0
            self.visited[i] = 1
            for j in self.edges[i]:
                maxDfs(j)
            
        def check_double_destruction(a,b,r1,c,d ) :
            dist = math.sqrt( (a-c)**2 + (b -d)**2 )
            if dist <= r1 :
                return True
            return False
            
        for i in range(len(bombs) - 1) :
            for j in range(i+1,n) :
                if check_double_destruction( bombs[i][0] , bombs[i][1] , bombs[i][2] ,bombs[j][0] , bombs[j][1]) :
                    self.edges[i].append(j)
                if check_double_destruction( bombs[j][0] , bombs[j][1] , bombs[j][2], bombs[i][0] , bombs[i][1]    ):
                    self.edges[j].append(i)
        
        ans =  0 
        for i in range(n):
            self.visited = [0 for i in range(n)]
            maxDfs(i)
            a = sum(self.visited)
            print(self.visited)
            ans=  max(ans,a)

        return ans