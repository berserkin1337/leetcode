class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        def merge(arr1,arr2):
            arr3 = [0]*(len(arr1) + len(arr2))
            i,j = 0,0
            curr = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    arr3[curr] = arr1[i]
                    i += 1
                else:
                    arr3[curr] = arr2[j]
                    j+=1
                curr += 1
            if i < len(arr1):
                while i < len(arr1):
                    arr3[curr] = arr1[i]
                    curr+=1
                    i+=1
            if j < len(arr2):
                while j < len(arr2):
                    arr3[curr] = arr2[j]
                    curr+=1
                    j+=1
            # print(arr1,arr2) 
            return arr3

        n = len(nums) 
        if nums[0] >= 0:
            return [num*num for num in nums]
        i = 0
        while i<n and nums[i]<0:
            i += 1
        neg = [-num for num in nums[:i]]
        neg.reverse()
        # print(neg)
        arr3 = merge(neg,nums[i:])
        # print(arr3)
        return [num*num for num in arr3]
