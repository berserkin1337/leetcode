class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        self.ans = -1
        self.visited = [False for i in range(n)]
        def dfs(i,dic):
            self.visited[i] = True
            if edges[i] == -1 :
                return
            if edges[i] in dic :
                self.ans =  max(self.ans, dic[i] - dic[edges[i]] + 1)
            elif not  self.visited[edges[i]]  :
                dic[edges[i]] = dic[i] + 1
                dfs(edges[i],dic)
            del dic[i]
        for i in range(n) :
            
            if  self.visited[i]  == False :
                dic = {}
                dic[i] = 0
                dfs(i, dic)
        return self.ans