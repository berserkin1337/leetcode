class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = [0 for i in range(len(queries))]
        nums = [0 for i in range(n)]
        nums[queries[0][0]] = queries[0][1]
        for i in range(1,len(queries)) :
            idx,val = queries[i]
            ans[i] = ans[i-1]
            if idx > 0 : 
                if nums[idx] != 0 and nums[idx] == nums[idx-1]  and nums[idx] != val :
                    ans[i] -= 1
                if val != nums[idx] and  val == nums[idx-1] :
                    ans[i] += 1
            if idx < n - 1  :
                if   nums[idx] != 0 and nums[idx] == nums[idx+1] and nums[idx] != val :
                    ans[i] -= 1
                if val != nums[idx] and val == nums[idx+1] :
                    ans[i] += 1
            
                 
            nums[idx] = val
            
        return ans