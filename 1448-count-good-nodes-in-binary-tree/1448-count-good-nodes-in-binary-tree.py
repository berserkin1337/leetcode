# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        self.ans = 0
        def dfs(root , largestVal):
            if root is None:
                return
            if root.val >= largestVal :
                self.ans += 1
                largestVal = root.val
            dfs(root.left,largestVal)
            dfs(root.right,largestVal)
        dfs(root,-float('inf'))
        return self.ans