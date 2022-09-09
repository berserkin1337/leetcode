class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        print(properties)
        n = len(properties)
        curMax = properties[-1][1]
        globMax = properties[-1][1]
        k = n-2
        while properties[k][0] == properties[k+1][0] and k >= 0:
            globMax = max(globMax,properties[k][1])
            k-= 1
        res = 0
        
        for i in range(k,-1,-1):
            if properties[i][0] != properties[i+1][0]:
                globMax = max(curMax, globMax)
                curMax = properties[i][1]
            else:
                curMax = max(curMax,properties[i][1])
            if globMax > properties[i][1] :
                res += 1
        return res