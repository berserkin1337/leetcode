class Solution:
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
            print(len(lookup))
            return False
        return func(s)