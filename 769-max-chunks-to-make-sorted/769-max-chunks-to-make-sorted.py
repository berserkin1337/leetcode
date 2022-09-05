class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        numChunk = 0
        curMax = 0
        for i in range(n):
            curMax = max(curMax,arr[i])
            numChunk += (curMax == i)
        return numChunk