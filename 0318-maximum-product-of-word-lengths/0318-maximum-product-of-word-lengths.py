class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        masks = []
        for word in words:
            x = set(word)
            mask = 0
            for i in range(26) :
                if chr(ord('a') + i) in x :
                    mask |= (1 << i)
            masks.append(mask)
        for i in range(1,len(words)) :
            for j in range(i):
                if masks[i] & masks[j] == 0 :
                    res = max(res,len(words[i])*len(words[j]))
        return res