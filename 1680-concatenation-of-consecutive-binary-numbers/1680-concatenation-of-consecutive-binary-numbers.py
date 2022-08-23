class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:
            return 1
        msb = n
        msb |= msb >> 1
        msb |= msb >> 2
        msb |= msb >> 4
        msb |= msb >> 8
        msb |= msb >> 16
        msb += 1
        return (self.concatenatedBinary(n-1)*(msb) + n)  % (10**9 + 7)