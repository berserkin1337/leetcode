class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if k == len(s) :
            return 0
        
        @cache
        def dfs (s, k) :
            if len(s)  <=  k :
                return 0
            if 1 <=len(s) <= 2 :
                if s[0] != s[-1] :
                    return 1
                else:
                    return 0
            if  k == 1 :
                res = 0
                for i in range(len(s) // 2 ) :
                    if s[i] != s[len(s) - 1 - i ] :
                        res += 1
                return res
            n = len(s)
            res = float('inf')
            for i in range(n-k  + 1) :
                newS = s[:i + 1]
                afS = s[i+1:]
                res = min( res,  dfs(newS,1) + dfs(afS,k-1))
                # if len(s) == 3 and k == 2 :
                #     print(dfs(newS,1) ,newS ,  dfs(afS,k-1) , afS )
            return res
        

        return dfs(s,k)