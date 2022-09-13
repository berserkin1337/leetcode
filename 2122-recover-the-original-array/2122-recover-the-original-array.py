class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        
        def check(nums,k):
            cnt, ans = Counter(nums) , []
            for num in nums:
                if cnt[num] == 0:
                    continue
                if cnt[num + k ] == 0:
                    
                    return False,[]
                cnt[num] -= 1
                cnt[num+k] -= 1
                ans.append(num+k//2)
            return True,ans
        n = len(nums)
        nums.sort()
        for i in range(1,n):
            k = nums[i] - nums[0]
            if k != 0 and k % 2 == 0 :
                a , b = check(nums,k)
                if a:
                    return b
                