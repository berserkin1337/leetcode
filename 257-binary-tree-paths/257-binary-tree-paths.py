# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode],) -> List[str]:
        self.res = []
        
        def listToStr(arr):
            s = ""
            for i in range(len(arr) - 1):
                s += str(arr[i])
                s+= "->"
            s += str(arr[-1])
            return s
            
        def paths(root,path):
            # print(root.val,path)
            if root.left is None and root.right is None:
                path.append(root.val)
                self.res.append(listToStr(path))
                path.pop()
                return
            path.append(root.val)
            if root.left:
                paths(root.left,path)
            
            if root.right:
                paths(root.right,path)
            path.pop()
        x = paths(root,[])
        return self.res