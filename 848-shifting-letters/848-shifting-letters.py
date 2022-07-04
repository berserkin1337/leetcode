class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix =  [0]*(len(shifts))
        prefix[-1] = shifts[-1]
        
        for i in range(len(shifts)-2,-1,-1):
            prefix[i] = prefix[i+1] + shifts[i]
        
        stringarr = list(s)
        
        
        for i in range(len(stringarr)):
            position = ord(stringarr[i]) - ord('a')
            final_position =( position + prefix[i]) % 26
            stringarr[i] = chr(ord('a') + final_position)
        return ''.join(stringarr)
            
        