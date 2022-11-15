# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        self.ans  = ""
        def dfs(root,curr="") :
            if not root:
                return
            curr = chr(root.val + ord('a')) + curr
            if root.left is None and root.right is None  :
                if len(self.ans) :
                    self.ans = min(self.ans ,  curr)
                else:
                    self.ans = curr
            dfs(root.left,curr)
            dfs(root.right,curr)
            curr = curr[1:]
        dfs(root)
        return self.ans