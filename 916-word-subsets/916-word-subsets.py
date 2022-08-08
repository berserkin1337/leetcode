from  collections import Counter




class Solution:
    # def _isSubset(self,word1,word2):
    #     counter = Counter(word1)
    #     for c  in  word2:
    #         if c in counter and counter[c]:
    #             counter[c] -= 1
    #         else:
    #             return False
    #     return True
    # def _checkSub(self,word1,arr):
    #     for word in arr:
    #         if not self._isSubset(word1 , word):
    #             return False
    #     return True
    def _checkCounter(self,wordCount , counter):
        for k in counter.keys():
            if counter[k] > wordCount[k]:
                return False
        return True
        
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        counter = Counter()
        
        for word in  words2:
            wordCount = Counter(word)
            for k in wordCount.keys():
                counter[k] = max(counter[k],wordCount[k])
        for word in words1:
            wordCount = Counter(word)
            if self._checkCounter(wordCount,counter):
                res.append(word)
        

        return res
        
        