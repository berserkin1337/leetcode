# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = collections.deque()
        queue.append(root)
        curMax , curRow, maxRow = -float('inf') ,0,0
        while queue:
            size = len(queue)
            newQueue = collections.deque()
            totalSum = 0
            for node in queue:
                totalSum += node.val
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            if totalSum > curMax:
                curMax = totalSum
                maxRow = curRow
            queue = newQueue
            curRow += 1
        return maxRow + 1