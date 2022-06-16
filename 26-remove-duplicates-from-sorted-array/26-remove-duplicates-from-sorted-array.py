class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 1:
            return 1
        j = 0
        s = set()
        i = 0
        for i in range(n):
            if nums[i] in s:
                while j <n and nums[j] in s:
                    j +=1
                    # print(i,j)
                    
                if j == n:
                    break
                nums[i],nums[j] = nums[j],nums[i]
            # print(nums[i])
            s.add(nums[i])
        # print(s)
        # print(i)
        if len(s) == n:
            return n
        return i
                        
            