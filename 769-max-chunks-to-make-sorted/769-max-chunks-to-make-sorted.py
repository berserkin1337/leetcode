class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        numChunk = 0
        for i in range(n):
            if sorted(arr[:i+1]) == [k for k in range(i+1)] :
                numChunk += 1
        return numChunk