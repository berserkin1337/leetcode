class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)
        if n < m:
            a,b = b,a
            
        # print(a,b)
        n = len(a)
        m = len(b)

        ans = ""
        i = 1
        carry = 0
        while i <= m:
            x = int(a[-i])
            y = int(b[-i])
            if x + y + carry == 3:
                ans = '1' + ans
                carry = 1
            elif x + y + carry == 2:
                ans = '0' + ans
                carry = 1
            elif x + y + carry == 1:
                ans = '1'  + ans
                carry = 0
            else:
                ans = '0' + ans
                carry = 0
            i += 1
        while i <= len(a):
            x = int(a[-i])
            if x + carry == 2:
                carry = 1
                ans = '0' + ans
            elif x + carry ==1:
                carry = 0
                ans = '1' + ans
            else:
                ans =  '0' + ans
            i += 1
        i -=1
        if carry != 0:
            ans = str(carry) + ans
        
        return ans
        