class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        # print(len(s) , n,s)
        ans = ""
        cur = s[0]
        cnt = 1
        for i in range(1,len(s)):
            if s[i] == cur:
                cnt += 1
            else:
                ans += str(cnt)
                ans += str(cur)
                cnt = 1
                cur = s[i]
        ans += str(cnt)
        ans += str(cur)
        return ans
        