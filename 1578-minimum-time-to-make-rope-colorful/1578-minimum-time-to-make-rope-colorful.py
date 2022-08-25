class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(neededTime)
#         dp = [0 for i in range(len(neededTime))]
#         dp[0] = 0
#         for i in range(1,n):
#             if colors[i] == colors[i-1]:
#                 j = i
#                 curr = 0
#                 maxi = -float('inf')
#                 while j>=1 and colors[j] == colors[j-1] :
#                     curr += neededTime[j]
#                     maxi = max(maxi , neededTime[j])
#                     j -= 1
                    
#                 curr += neededTime[j]
#                 maxi = max(maxi , neededTime[j])
#                 j -= 1
#                 # print(i,j,curr , maxi)
#                 if j >= 0:
#                     dp[i]  = dp[j] + curr - maxi
#                 else:
#                     dp[i] = curr - maxi
#             else:
#                 dp[i] = dp[i-1]
        # print(dp)
        # return dp[-1]
        
        res = 0
        i = 0 
        while i < n - 1 :
            if colors[i] == colors[i+1] :
                
                curr = 0
                maxi = -float('inf')
                j = i
                while j < n:
                    curr += neededTime[j]
                    maxi = max(maxi , neededTime[j])
                    if j < n- 1 and  colors[j] != colors[j+1]:
                        break
                    j += 1
                res += curr - maxi
                i = j
                i += 1
            else:
                i += 1
        
        return res