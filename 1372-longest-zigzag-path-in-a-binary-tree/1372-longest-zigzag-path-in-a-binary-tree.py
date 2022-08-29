# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:	
        self.ans = 0
        
        @cache
        def recurse(root):
            if not root: return (-1,-1) 
            l1,r1 = recurse(root.left)
            l2,r2 = recurse(root.right)
            self.ans = max(self.ans, max(r1 + 1, l2 + 1))
            return (r1 + 1, l2 + 1)
			
        recurse(root)
        return self.ans
