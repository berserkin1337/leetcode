class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32) :
            bita =  ( a >> i ) & 1 
            bitb =  (b >> i ) & 1
            bitc= (c >> i) & 1
            if  bita == 0 and bitb == 0 and bitc == 1 :
                ans += 1
            if bita == 1 and bitb == 1 and bitc == 0 :
                ans += 2
            if bitc == 0  and (( bita == 0 and bitb == 1 )  or  ( bita  == 1 and bitb == 0 ) ) :
                ans += 1
        return ans
