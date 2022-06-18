class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        solutions =set()
        for i in range(n):
            dic = {}
            
            for j in range(i):  
                if nums[j] in dic:
                    solutions.add(tuple(sorted((nums[i],nums[j],dic[nums[j]]))))
                        # res.append([nums[i],nums[j],dic[nums[j]]])
                else:
                    dic[-(nums[j]+nums[i])] = nums[j]
                    
        return [list(s) for s in solutions]