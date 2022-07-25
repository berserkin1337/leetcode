class Solution:
    def maxAbsValExpr(self, arr1: list, arr2: list) -> int:
        a = [arr1[i] + arr2[i] + i for i in range(len(arr1))]
        b = [arr1[i] + arr2[i] - i for i in range(len(arr1))]
        c = [arr1[i] - arr2[i] + i for i in range(len(arr1))]
        d = [arr1[i] - arr2[i] - i for i in range(len(arr1))]
        return max(map(lambda x: max(x) - min(x), (a, b, c, d)))
