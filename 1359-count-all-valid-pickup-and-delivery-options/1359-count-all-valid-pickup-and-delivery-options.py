class Solution:
    def countOrders(self, n):
        return (math.factorial(n * 2) >> n) % (10**9 + 7)
