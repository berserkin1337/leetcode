class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while (n != 0) :
            ans  += (1 if n & 1 > 0 else 0)
            # print(ans,n)
            n //= 2
        return ans