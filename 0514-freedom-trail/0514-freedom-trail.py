class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        indices = defaultdict(list)
        for i , c in enumerate(ring) :
            indices[c].append(i)
        
        q = []
        for a in indices[key[0]] :
            q.append((a,min(a,len(ring)-a)  + 1 ))
        for  i in range(1,len(key)) :
            newQ = []
            x = defaultdict(lambda: float('inf'))
            for (a,b) in q:
                for j in indices[key[i]] :
                    if j >= a :
                        x[j] = min(x[j], a + len(ring) - j + 1  + b)
                        x[j] = min(x[j], j - a + 1 + b)
                    else:
                        x[j] = min(x[j],a - j + 1 + b)
                        x[j] = min(x[j],len(ring) - a  + j + 1 + b)
            for a in indices[key[i]] :
                if x[a] != float('inf') :
                    newQ.append((a,x[a]))
            q = newQ
        return min([b for a,b in q])