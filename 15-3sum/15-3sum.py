class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n):
            dic = {}
            
            for j in range(i):  
                if nums[j] in dic:
                    if [nums[i],nums[j],dic[nums[j]]] not in res:
                        res.append([nums[i],nums[j],dic[nums[j]]])
                else:
                    dic[-(nums[j]+nums[i])] = nums[j]
        return res