# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def inSubTree(self,root,p):
        if root == p:
            return True
        if root is None:
            return False
        return self.inSubTree(root.left , p)  | self.inSubTree(root.right , p)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root.val > p.val and root.val > q.val :
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < p.val and root.val < q.val :
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        
        