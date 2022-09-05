"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = []
        res = []
        queue.append(root)
        while queue :
            newQueue = []
            queueVal = []
            for node in queue:
                queueVal.append(node.val)
                for child in node.children:
                    newQueue.append(child)
                    
            res.append(queueVal)
            queue = newQueue
        return res
            