class Solution:


    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def dp(steps,mask):
            if steps > len(nums) // 2 : 
                return 0
            maxans = 0
            for i in range(len(nums)-1):
                if  ((mask >> i & 1 ) == 1) :
                    continue
                
                for j in range(i+1,len(nums)):
                    
                    if (( mask >> j & 1 )== 1) :
                        continue
                    
                    newMask = mask | ( 1 << i ) | ( 1 << j)
                    current = steps * math.gcd(nums[i],nums[j])
                    maxans = max (current + dp(steps+1,newMask) , maxans )
                    
            return maxans
        return dp(1,0)
