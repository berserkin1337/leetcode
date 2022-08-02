class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currMax = strs[0]
        def maxCommon(str1, str2) :
            curr = ""
            for i in range(min(len(str1) , len(str2))):
                if str1[i] == str2[i]:
                    curr += str1[i]
                else:
                    break
            return curr
        
        for i in range(1,len(strs)):
            print(currMax)
            currMax = maxCommon(currMax,strs[i])
        return currMax