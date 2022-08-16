class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, c in enumerate(s):
            if c in dic:
                (idx, num )= dic[c]
                dic[c] = (idx,num+1)
            else:
                dic[c] = (i,1)
        
        for key,val in dic.items():
            (idx,num) = val
            if num == 1:
                return idx
        return -1