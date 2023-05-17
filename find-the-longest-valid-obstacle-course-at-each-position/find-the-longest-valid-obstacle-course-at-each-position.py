class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [1]
        res = [obstacles[0]]
        for i in range(1,n):
            if res[-1] <= obstacles[i] :
                res.append(obstacles[i])
                ans.append(len(res))
            else:
                idx = bisect_right(res,obstacles[i])
                res[idx] = obstacles[i]
                ans.append(idx+1)
        return ans