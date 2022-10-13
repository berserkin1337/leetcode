class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s),len(t)
        cnt = collections.Counter(t)
        left = 0
        cur  = len(cnt)
        res = float('inf')
        resStr  = (-1,-1)
        
        for i in range(m):
            if s[i] in cnt :
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0  :
                    cur -= 1
            while left  < m and cur == 0 :
                if i - left + 1 < res :
                    resStr = (left,i)
                    res = i - left + 1
                if s[left] in cnt : 
                    cnt[s[left]] += 1
                    if cnt[s[left]] > 0 :
                        cur += 1
                left += 1
        return s[resStr[0]:resStr[1] + 1]