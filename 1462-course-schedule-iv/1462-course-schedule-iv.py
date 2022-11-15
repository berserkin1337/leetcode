class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqs  = defaultdict(set)
        cnt = [0 for  i in range(numCourses)]
        
        for [a,b] in prerequisites :
            prereqs[b].add(a)
            cnt[a] += 1
        newReqs = defaultdict(set)
        @cache
        def dfs(node):
            ans  = set()
            for u in prereqs[node]:
                ans |= dfs(u)
            ans.add(node)
            return ans
        for  i in range(numCourses):
            newReqs[i] = dfs(i)
        res = []
        for [a,b] in queries:
            res.append((a in newReqs[b]))
        return res