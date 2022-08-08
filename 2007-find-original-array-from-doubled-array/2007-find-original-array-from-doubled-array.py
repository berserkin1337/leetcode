class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        lookup = collections.Counter(changed)
        print(lookup)
        res = []
        for k in lookup.keys():
            if k == 0:
                res += [0] * (lookup[k]//2)
                if lookup[k] % 2 != 0:
                    return []
            elif lookup[k] > 0:
                
                x = k
                while x % 2== 0 and x//2 in  lookup:
                    x //= 2
                while x in lookup :
                    if lookup[x] > 0:
                        res += [x]* lookup[x]
                        if lookup[x+x] < lookup[x]:
                            return []
                        lookup[x+x] -= lookup[x]
                        lookup[x] = 0
                    x+=x
        return res
        
        
        
        