# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def MaxAmount(root):
            if root is None:
                return 0
            if root in dp:
                return dp[root]
            op1 = MaxAmount(root.left) + MaxAmount(root.right)
            op2 = root.val
            if root.left is not None:
                op2 += (MaxAmount(root.left.left) + MaxAmount(root.left.right))
            if root.right is not None:
                op2 += (MaxAmount(root.right.left) + MaxAmount(root.right.right))
            
            
            dp[root] = max(op1,op2)
            return dp[root]
        
        return MaxAmount(root)