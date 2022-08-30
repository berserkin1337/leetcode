class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low  = 0 
        high = n - 1
        while low <= high :
            mid = (low+high) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            elif arr[mid-1] > arr[mid] :
                high  = mid - 1
        if low == high:
            return (low)
        return -1