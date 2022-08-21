# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        @cache
        def generateBst(l,r) :
            if r < l :
                return [None]
            if r==l:
                return [TreeNode(l)]
            res = []
            for i in range(l,r + 1):
                listOfBsts1  =   generateBst(l,i-1)
                listOfBsts2 = generateBst(i+1,r)
                for k in range(len(listOfBsts1)):
                    for j in range(len(listOfBsts2)):
                        newNode = TreeNode(i,listOfBsts1[k],listOfBsts2[j])
                        res.append(newNode)
            return res
        return list(set(generateBst(1,n)))
         