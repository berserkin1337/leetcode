class Solution:
    def minDeletions(self, s: str) -> int:
        arr = [0]*(26)
        for c in s:
            arr[ord(c)-ord('a')] +=1
        s = set(arr)
        numzero = arr.count(0)
        # print(numzero,len(s) , len(arr))
        if len(arr) - len(s) == numzero -1 :
            return 0
        dic = {}
        ans = 0
        for i,num in enumerate(arr):
            if num == 0:
                continue
            if num in dic:
                
                while (arr[i] in s or arr[i]  in dic) and arr[i]>0  :
                    arr[i] -= 1
                    ans += 1
                dic[arr[i]] = 1
                print(arr[i],i)
            else:
                dic[arr[i]] = 1
        return ans