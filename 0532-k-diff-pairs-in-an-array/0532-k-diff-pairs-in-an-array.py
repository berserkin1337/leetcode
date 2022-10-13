class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        curr = set()
        res = 0
        dic = set()
        for num in nums :
            # print(dic,num)
            if num in dic :
                if (num-k,num) not in curr :
                    res += 1 
                curr.add((num-k,num))
            
            dic.add(num + k)
        return res
            