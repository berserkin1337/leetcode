class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        """
        text = "ghiabcdefhelloadamhelloabcdefghi"
        
        """
        @cache
        def dfs(s) :
            # print(s)
            if len(s)  == 0:
                return 0
            if len(s) == 1 :
                return 1
            if len(s) == 2:
                if s[0] == s[-1] :
                    return 2
                else:
                    return 1

            n = len(s)
            i,j = 0 , n - 1
            res = 1 
            while i < j :
                if s[:i+1] == s[j:] :
                    res = max(res , 2 + dfs(s[i+1:j]))
                i ,j = i + 1 , j - 1
            return res
        return dfs(text)
                    