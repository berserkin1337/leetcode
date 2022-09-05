class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n,m = len(difficulty) , len(worker)
        worker.sort()
        i = n-1
        j = m-1
        res = 0
        zipped  = zip(difficulty,profit)
        zipped = list(sorted( zipped , key = lambda x : x[1]))
        print(zipped)
        while i >= 0 and j >= 0:
            if worker[j] < zipped[i][0]:
                while i >= 0 and worker[j] < zipped[i][0]:
                    i -= 1
            else:
                res += zipped[i][1]
                
                j -= 1
        return res