class Solution:
    def longestAwesome(self, s: str) -> int:
        maskSet = {}
        maskSet[0] =  0
        mask = 0
        ans = 0
        for i in range(len(s)):
            curPos = int(s[i])
            mask ^= (1 << curPos)
            if mask not in maskSet:
                maskSet[mask] = i + 1
            else:
                ans = max(ans , i  - maskSet[mask] + 1)
            for j in range(10):
                if mask ^ (1 << j ) in maskSet:
                        ans = max(ans,  i - maskSet[mask ^ (1 << j )] + 1)
        
        return ans