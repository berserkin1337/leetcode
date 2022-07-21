class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def sortFunc(e):
            return len(e)
        words.sort(key=sortFunc)
        # print(len(words))
        res = []
        preWords = words[::]
        preWords.pop()
        # print(preWords)
        # print(len(words))
        for i in range(len(words)-1,-1,-1):
            if(self.wordBreak(words[i],preWords)):
                res.append(words[i])
            # print("hi")
            if len(preWords)!=0:
                preWords.pop()
        return res
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            global lookup
            global dictionary
            dictionary = set(wordDict)
            lookup = set()

            def func(s):
                if s in lookup:
                    return False
                if len(s) == 0:
                    return True
                for idx in range(1, len(s)+1):
                    if s[:idx] in dictionary:
                        if func(s[idx:]):
                            return True
                lookup.add(s)
                return False
            return func(s)
