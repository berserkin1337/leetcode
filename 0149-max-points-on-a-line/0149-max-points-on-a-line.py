class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1 :
            return n
        lines = defaultdict(set)
        for i in range(1,len(points)):
            for j in range(i) :
                if points[i][0] != points[j][0] :
                    slope = (points[i][1] - points[j][1])  /  (points[i][0] - points[j][0])
                    intercept = points[i][1] - (slope*points[i][0])
                    lines[(slope,intercept)].add((points[i][0],points[i][1]))
                    lines[(slope,intercept)].add((points[j][0],points[j][1]))
                else :
                    slope = float('inf')
                    intercept = points[i][0]
                    lines[(slope,intercept)].add((points[i][0],points[i][1]))
                    lines[(slope,intercept)].add((points[j][0],points[j][1]))

        return max(len(lines[key])  for key in lines)