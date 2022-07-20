class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        global dictionary
        dictionary = set(wordDict)
        
        @cache
        def func(s):
            if len(s) == 0:
                return True
            for idx in range(1, len(s)+1):
                if s[:idx] in dictionary:
                    if func(s[idx:]):
                        return True

            return False
        return func(s)