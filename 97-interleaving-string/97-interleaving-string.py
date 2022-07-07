class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self._interLeave(s1,s2,s3)
    
    @cache
    def _interLeave(self,s1,s2,s3):
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
        
        if(len(s1) != 0  and len(s2) != 0 and len(s3)!=0 ) and s1[-1] == s2[-1]  and s1[-1] == s3[-1]:
            res1 = self._interLeave(s1[:-1],s2,s3[:-1])
            res2 = self._interLeave(s1,s2[:-1],s3[:-1])
            return res1 | res2
        
        elif len(s1) != 0 and len(s3) != 0 and  s1[-1] == s3[-1]:
            return self._interLeave(s1[:-1],s2,s3[:-1])
        elif len(s2) != 0 and len(s3) != 0 and  s2[-1] == s3[-1]:
            return self._interLeave(s1,s2[:-1],s3[:-1])
        else:
            return False
        
            