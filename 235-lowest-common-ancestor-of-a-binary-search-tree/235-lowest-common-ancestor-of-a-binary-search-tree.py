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
        
        left1 = self.inSubTree(root.left,p) & self.inSubTree(root.left,q)
        right1 = self.inSubTree(root.right,p) & self.inSubTree(root.right,q)
        
        if( not left1) & (not right1) :
            return root
        elif left1:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)
        
        