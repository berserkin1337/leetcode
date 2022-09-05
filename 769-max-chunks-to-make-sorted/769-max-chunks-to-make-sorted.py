class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        targetArr = []
        numChunk = 0
        for i in range(n):
            targetArr.append(i)
            if sorted(arr[:i+1]) == targetArr :
                numChunk += 1
        return numChunk