class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        maskSet = collections.defaultdict(int)
        maskSet[0] = 1
        mask = 0
        ans = 0
        for i in range(len(word)):
            curPos = ord(word[i]) - ord('a')
            mask ^= (1<<curPos)
            ans += maskSet[mask]
            maskSet[mask] += 1
            for j in range(10):
                ans += maskSet[mask ^ (1<<j)]
                    
        
        
        return ans