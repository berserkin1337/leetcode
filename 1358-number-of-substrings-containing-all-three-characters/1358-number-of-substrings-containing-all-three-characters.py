class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        dic  = {}
        ans = 0
        min_pos = -1
        for i,c in enumerate(s):
            dic[c] = i
            if "a" in dic and "b" in dic and "c" in dic:
                min_pos = min(dic['a'],dic['b'],dic['c'])
            else:
                min_pos = -1
            ans +=( min_pos + 1)
            print(ans)
            
        return ans
        
        