class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i , j  , curr,res = 0 ,  0 , 0 , 0
        for j in range(len(nums)):
            curr += nums[j]
            while( curr + k)  < (j - i + 1) * nums[j]:
                curr -= nums[i]
                i += 1
            res = max(res, j- i +1 )
        return res