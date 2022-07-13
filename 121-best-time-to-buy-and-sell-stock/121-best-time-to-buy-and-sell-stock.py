class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # curr = max(curr,prices[i]-min)
        mini = prices[0]
        curr = 0
        for i in range(1,n):
            mini = min(prices[i],mini)
            if prices[i] == mini:
                continue
            
            curr = max(curr,prices[i]-mini)
        
        return curr