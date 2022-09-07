# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = ""
        def preOrder(root):
            if root is None:
                return
            self.ans  += str(root.val)
            if root.left is None and root.right is None:
                return
            self.ans += "("
            if root.left is not None:
                preOrder(root.left)
            self.ans += ")"
            if root.right is not None:
                self.ans += "("
                preOrder(root.right)
                self.ans += ")"
            
        preOrder(root)
        return self.ans