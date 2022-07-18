class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books) 
        dp = [0]*(n)
        """
        books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]] ,  shelfWidth = 4
        books[i] = [thickness,height]
        dp[0] = books[0][1] = 1
        dp[1] = max(3,1)  = 3
        dp[2] = 1 + 
        """
        dp[0] = books[0][1]

        for i in range(1,n):
            maxHeight = books[i][1]
            currWidth = books[i][0]
            j = i- 1
            dp[i] = dp[j] + maxHeight
            while j >=0 :
                if currWidth + books[j][0] > shelfWidth:
                    break
                currWidth += books[j][0]
                maxHeight = max(maxHeight,books[j][1])
                j-=1 
                dp[i] = min(dp[i],dp[j]+maxHeight)

            if j < 0:
                dp[i]= maxHeight

            else:
                dp[i] =min( dp[j] + maxHeight,dp[i])
        # print(dp)
        return dp[-1]
