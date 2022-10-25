import copy
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        cnt = Counter(words)
        res = []
        totalWords = len(words)
        for i in range(len(s) - totalWords*n+1):
            z  = defaultdict(int)
            
            for j in range(totalWords) :
                wordIdx = i + j * n
                word = s[wordIdx:wordIdx+n]
                if word not in cnt :
                    break
                z[word] += 1
                if z[word] > cnt[word] :
                    break
                if j + 1 == totalWords :
                    res.append(i)
                
        return res