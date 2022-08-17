class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # dp[i] = length of the longest substring at  i
        # dp = [0 for  i in range(len(p))]
        # if len(p) == 1:
        #     return 1
        res = 1
        curr = 1
        dic = {}
        dic[p[0]] = 1
        for i in range(1,len(p)):
            
            if ord(p[i]) -  ord( p[i-1]) == 1 or (p[i] == 'a'  and p[i-1] == 'z') :
                curr += 1
            else:
                curr = 1
            if p[i] not in dic:
                dic[p[i]] = curr
            else:
                dic[p[i]] = max(dic[p[i]], curr)
        res = 0
        for c,length in dic.items():
            res += length
        # print(dic)
        return res
            
        