# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        self.lookup = dict()
        self.lookup[1] = [TreeNode(0)]
        def fbt(num):
            if num in self.lookup:
                return self.lookup[num]
            if num % 2 == 0:
                return []
            if num  == 1:
                node = TreeNode(0)
                self.lookup[1] = [node]
                return [node]

            res = []
            for i in range(1,num,2):
                for leftNode in fbt(i):
                    for rightNode in fbt(num-1-i):
                        node = TreeNode(0)
                        node.left = leftNode
                        node.right = rightNode
                        res.append(node)
            self.lookup[num] = res
            return res                
                
        return fbt(n)