class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        nums = 0
        while (minutesToTest/minutesToDie + 1)**nums <  buckets:
            nums += 1
        return nums