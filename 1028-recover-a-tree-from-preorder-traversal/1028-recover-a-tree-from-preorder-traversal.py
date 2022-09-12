# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i , stack = 0, []
        
        while i < len(traversal) :
            # print(stack)
            level , val  = 0 , ""
            while i < len(traversal) and traversal[i] == '-' :
                level , i = level  + 1, i + 1
            while i < len(traversal) and traversal[i] != '-' :
                val , i = val  + traversal[i] , i + 1
            val = int(val)
            while len(stack) > level :
                stack.pop()
            
            node = TreeNode(val)
            if len(stack) and stack[-1].left is None:
                stack[-1].left = node
            elif len(stack):
                stack[-1].right = node
            stack.append(node)
        return stack[0]