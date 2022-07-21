class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        dp[i] = length of longest word chain ending at index i
        words = ["a","b","ba","bca","bda","bdca"]
        dp[0] = 1
        dp[1] = 1
        
        """
        #check if word1 is predecessort to word2
        
        def isPred(word1,word2):
            if len(word2) - len(word1) != 1:
                return False
            cnt = 0
            i = 0
            j = 0
            while i < len(word1) and j < len(word2) :
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                else:
                    j+=1
                    cnt += 1
                    if cnt >=2:
                        return False
            return True
        def sortFunc(e):
            return len(e)
        words.sort(key=sortFunc)
        predCount = [1]*len(words)
        for i in range(len(words)):
                for j in range(i):
                    if isPred(words[j],words[i]):
                        predCount[i] = max(predCount[i],predCount[j]+1)
            
            
        return max(predCount)
            