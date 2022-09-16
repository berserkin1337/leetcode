# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        self.view = {}
        self.maxLevel = -1
        def dfs(node,level):
            if node is None:
                return
            if level not  in  self.view :
                self.view[level]  = node.val
            self.maxLevel = max(level,self.maxLevel)
            dfs(node.right,level + 1)
            dfs(node.left,level + 1)
        dfs(root,0)
        return [self.view[level] for level in range(self.maxLevel+1)]