# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        @cache
        def hasOne(root):
            if root is None:
                return False
            if root.val == 1:
                return True
            else:
                return (hasOne(root.left) or hasOne(root.right) )
        # print(hasOne(node.right))

        def mkTree(root):
            if root is None:
                return None
            leftNode = mkTree(root.left)
            rightNode = mkTree(root.right)
            newNode = TreeNode(root.val,leftNode,rightNode)
            return newNode
        def prune(root):
            if hasOne(root):
                leftNode = prune(root.left)
                rightNode = prune(root.right)
                # print(root.val,leftNode,rightNode)
                newNode = TreeNode(root.val , leftNode,rightNode)
                return newNode
            else:
                return None
        return prune(node)