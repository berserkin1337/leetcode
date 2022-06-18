class Solution:
    
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr = deque()
        j = 0
        ans = 0
        for i,c in enumerate(nums):
            # print(len(curr))
            if c == 1:
                ans = max(i-j+1,ans)
            else:
                if len(curr) < k:
                    ans = max(i-j+1,ans)
                    curr.append(i)
                    
                else:
                    curr.popleft()
                    curr.append(i)
                    j = curr[0]
                    j-=1
                    
                    while j >=0 and nums[j] == 1:
                        j -=1
                    j+=1
                    print(j,i)
                    ans = max(i-j+1,ans)
            # print(ans)
        return ans