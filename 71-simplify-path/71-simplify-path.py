class Solution:
    def simplifyPath(self, path: str) -> str:

        def nextPath(s):
            i = 0
            while i < len(s) and s[i] == '/'  :
                i += 1
            start = i
            while i < len(s) and s[i] != '/':
                i+=1
            end = i
            resStr = s[start:end]
            
            while i < len(s) and  s[i] == '/' :
                i += 1
                
            return [resStr,i]
        n = len(path)
        res = []
        
        i = 0
        while i < len(path):
            # print(path[i])
            [nextStr,j] = nextPath(path[i:])
            i += j
            if nextStr == '.':
                continue
            elif nextStr == '..':
                if len(res) != 0:
                    res.pop()
            else:
                res.append(nextStr)
        return "/" + "/".join(res)
        