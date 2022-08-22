# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def mkTree(root):
            if root is None:
                return None
            leftTree = mkTree(root.left)
            rightTree = mkTree(root.right)
            if leftTree is None and rightTree is None and root.val == target :
                return None
            newNode =  TreeNode(root.val,leftTree,rightTree)
            return newNode
        return mkTree(root)
            
                        
        