# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        def delete(node,parent):
            if node is None:
                return
            if node.val == key :
                if node.right is not None:
                    temp = node.left
                    curRoot = node.right
                    if parent is not None:
                        if parent.left == node:
                            node.left = temp
                            parent.left = node.right
                        else:
                            parent.right = node.right
                    leftNode = curRoot
                    while leftNode.left is not None:
                        leftNode = leftNode.left
                    leftNode.left  = temp
                else:
                    curRoot = node.left
                    if parent is not None:
                        if parent.left == node:
                            parent.left = curRoot
                        else:
                            parent.right = curRoot
            else:
                delete(node.left,node)
                delete(node.right, node)
        delete(root,None)
        if root.val != key:
            return root
        else:
            if root.right is not None:
                return root.right
            else:
                return root.left