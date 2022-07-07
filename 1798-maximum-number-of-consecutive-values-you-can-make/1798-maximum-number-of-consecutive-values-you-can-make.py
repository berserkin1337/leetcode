class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ans = 1
        coins.sort()
        for coin in coins:
            if coin > ans:
                break
            
            ans += coin
        
        return ans
        
                