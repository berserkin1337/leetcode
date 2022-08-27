class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        self.counted = set()
        self.nopali = set()
        def palindrome(i,j):
            if i > j:
                return False
            if i == j:
                self.counted.add((i,j))
                return True
            
            if (i,j) in self.counted:
                return True
            elif (i,j) in self.nopali :
                return False
            # print(i,j)
            if s[i] == s[j]:
                if palindrome(i+1,j-1) or i == j-1 :
                    self.counted.add((i,j))
                    return True
                else:
                    self.nopali.add((i,j))
                    return False
            else:
                self.nopali.add((i,j))
                return False
        
        for i in range(n):
            for j in range(n-1,i-1,-1):
                palindrome(i,j)
        
        # print(self.counted)
        return len(self.counted)