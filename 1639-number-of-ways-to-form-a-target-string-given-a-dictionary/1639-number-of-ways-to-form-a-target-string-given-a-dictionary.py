class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = int(1e9 + 7)
        
        curr = [0 for i in range(len(words))]
        
        freq  = [[0 for  i in range(26)] for  j in range(len(words[0]))]
        for  i in range(len(words[0])):
            for j  in range(len(words)) :
                freq[i][ord(words[j][i]) - ord("a")] += 1
        
        dp = [freq[i][ord(target[-1]) - ord("a")]  for  i in range(len(words[0]))]
        
        for i  in range(len(target)-2,-1,-1):
            
            newDp = [0 for i in range(len(words[0]))]
            suffix = dp[-1]
            for j in range(len(words[0]) - 2, -1,-1) :
                newDp[j] =  (suffix * freq[j][ord(target[i]) - ord("a")])
                suffix += (dp[j])
            dp = newDp[::]
            
        return sum(dp[:len(words[0]) - len(target) + 1]) % MOD