class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s,res,path):
            if len(s) == 0:
                res.append(path)
                return
            
            for i in range( len(s)):
                currStr = s[:i+1]
                if currStr == currStr[::-1] :
                    dfs(s[i+1:],res,path + [s[:i+1]])
        res = []
        dfs(s,res,[])
        return res