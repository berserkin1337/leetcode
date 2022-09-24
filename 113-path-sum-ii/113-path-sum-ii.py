# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.res = []
        def curPath(root,curr,path):
            if root is None:
                return
            if root.left is None and root.right is None :
                path.append(root.val)
                curr += root.val
                if curr == targetSum:
                    self.res.append(path[::])
                    # print(root.val)
                path.pop()
                curr -= root.val
                return
            path.append(root.val)
            curr += root.val
            curPath(root.left,curr,path)
            curPath(root.right,curr,path)
            path.pop()
            curr -= root.val
        curPath(root,0,[])
        return self.res