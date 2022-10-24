class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        self.target = 24

        def backtrack(curr):
            if len(curr) ==  1 :
                if curr[0] >= 23.99999 and curr[0] <= 24.00001 :
                    return True
            
            for  i in range(len(curr)) : 
                for  j in range(len(curr)):
                    if i == j :
                        continue
                    x = curr[::]
                    x.remove(curr[i])
                    x.remove(curr[j])
                    x.append(curr[i]+curr[j])
                    if backtrack(x):
                        return True
                    x.pop()
                    x.append(curr[i] - curr[j])
                    if backtrack(x) :
                        return True
                    x.pop()
                    x.append(curr[j] - curr[i])
                    if backtrack(x):
                        return True
                    x.pop()
                    x.append(curr[i]*curr[j])
                    if backtrack(x):
                        return True
                    x.pop()
                    if curr[i] != 0 :
                        x.append(curr[j]/curr[i])
                        if backtrack(x):
                            return True
                        x.pop()
                    if curr[j]  != 0 :
                        x.append(curr[i]/curr[j])
                        if backtrack(x):
                            return True
                        x.pop()
            return False
        return  backtrack(cards)
