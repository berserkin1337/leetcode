class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        counts = Counter(nums)
        s = set(nums)
        
        nums = sorted(list(s))
        n = len(nums)
        i = 0
        while i < n:
            if counts[nums[i]] == 0:
                i += 1
                continue
            for j in range(k):
                if nums[i] + j not in counts or (counts[nums[i] + j] <= 0):
                    print(i)
                    return False
                counts[nums[i] + j] -= 1
        for key in counts:
            if counts[key] > 0:
                return False
        return True