class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]*(len(arr))
        
        for i,num in enumerate(arr):
            prefix[i] = prefix[i-1] ^ num
        # print(prefix)
        res = []
        for num1 , num2 in queries :
            if num1 == num2:
                res.append(arr[num1])
            else:
                if num1 == 0:
                    res.append(prefix[num2])
                else:
                    res.append(prefix[num1-1]^prefix[num2])
        
        
        return res
        
        
        