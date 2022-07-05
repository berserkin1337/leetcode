# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # Inorder traversal O(1)
        global ans
        ans = 0
        def inorder(Root):
            global ans
            if Root == None:
                return 
            
            inorder(Root.left)
            ans +=1
            inorder(Root.right)
            return
        
        inorder(root)
        return ans