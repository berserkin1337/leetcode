class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt=  Counter(arr)
        arr.sort(key = lambda x: abs(x))
        for num in arr:
            # print(num,cnt)
            if cnt[num] == 0:
                continue
            if cnt[num*2] == 0:
                return False
            cnt[num] -= 1
            cnt[num*2] -= 1
        
        
        return True