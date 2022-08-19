class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        mp = {}
        for i,name in enumerate(names):
            if name  in mp:
                minVal = mp[name]
                while name+"(" + str(minVal) + ")" in mp:
                    minVal+=1
                names[i] = name + "(" + str(minVal) + ")"
                mp[name] = minVal+1
                mp[names[i]] = 1
            else:
                mp[names[i]] = 1
                
        return names