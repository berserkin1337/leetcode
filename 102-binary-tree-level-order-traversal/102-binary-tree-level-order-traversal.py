# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None :
            return []
        queue = []
        queue.append(root)
        res = []
        dic = defaultdict(int)
        dic[root] = 1
        while queue:
            topNode = queue.pop(0)
            if len(res) < dic[topNode]:
                res.append([topNode.val])
            else:
                res[dic[topNode] -1].append(topNode.val)
            if topNode.left:
                queue.append(topNode.left)
                dic[topNode.left] = dic[topNode] + 1
            if topNode.right:
                queue.append(topNode.right)
                dic[topNode.right] = dic[topNode] + 1
        return res