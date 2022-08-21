# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def getMin(self,root):
        if root is None:
            return float('inf')
        curr = root.val
        return min(curr,self.getMin(root.left),self.getMin(root.right))
    
    @cache
    def getMax(self,root):
        if root is None:
            return -float('inf')
            
        curr = root.val
        return max(curr,self.getMax(root.left),self.getMax(root.right))
    
    @cache
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        
        mini1 = self.getMin(root.left) if root.left is not None else root.val
        maxi1 = self.getMax(root.left) if root.left is not None else root.val
        mini2 = self.getMin(root.right) if root.right is not None else root.val
        maxi2 = self.getMax(root.right) if root.right is not None else root.val
        
        maxDiff1 = max(abs(root.val - mini1) , abs(root.val - maxi1))
        maxDiff2 = max(abs(root.val - mini2) , abs(root.val - maxi2))
        maxDiff = max(maxDiff1 , maxDiff2)
        val1 = -float('inf')
        if root.left is not None:
            val1 = self.maxAncestorDiff(root.left)
        val2 = -float('inf')
        if root.right is not None:
            val2 = self.maxAncestorDiff(root.right)
        return max(maxDiff,val1,val2)
        
        
        