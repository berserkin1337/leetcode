class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        self.lookup = {}        
        def dfs(l,r):
            if l == r:
                return 0
            elif r - l == 1 :
                return arr[l] * arr[r]
            if (l,r) in self.lookup:
                return self.lookup[(l,r)]
            ans = float('inf')
            for i in range(l,r):
                curr = max(arr[l:i+1]) * max(arr[i+1:r+1])
                curr += dfs(l,i) + dfs(i+1,r)
                # print(curr)
                ans = min(ans,curr)
            self.lookup[(l,r)] = ans
            return ans
        
        ans =  dfs(0,len(arr) - 1)
        print(self.lookup)
        return ans