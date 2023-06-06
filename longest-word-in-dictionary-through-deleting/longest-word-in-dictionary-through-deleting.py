class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        # check if a is a subsequence of b
        def is_subsequence(a:str, b : str) :
            i,j = 0,0
            while i != len(a) and j != len(b) :
                if a[i] == b[j] :
                    i += 1
                j += 1  

            return i>= len(a)
        
        ans = ""
        

        for word in dictionary : 
            if is_subsequence(word,s) :
                if len(word) > len(ans)  or  (len(word) == len(ans) and (ans  > word)):
                    ans = word
        return ans
                    