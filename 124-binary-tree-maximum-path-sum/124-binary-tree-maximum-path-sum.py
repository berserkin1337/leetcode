# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = -float('inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def maxSum(root):
            if root is None :
                return 0
            a = maxSum(root.left)
            b = maxSum(root.right)
            ans = max(a , 0) + root.val + max(b , 0)
            self.res = max(self.res,ans)
            
            # print(root.val,ans,a,b)
            return max(root.val + a,root.val + b,root.val)   
        maxSum(root)
        return self.res