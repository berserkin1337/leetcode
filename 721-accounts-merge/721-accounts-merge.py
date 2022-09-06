class UF:
    def __init__(self,N):
        self.parents = list(range(N))
    def find(self,v):
        if v != self.parents[v]:
            self.parents[v] = self.find(self.parents[v])
        return self.parents[v]
    def union(self,a,b):
        self.parents[self.find(b)] = self.find(a)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        ownership = {}
        
        for i , (_,*emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i,ownership[email])
                ownership[email] = i
        
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
