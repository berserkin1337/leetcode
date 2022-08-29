# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        
        @cache
        def contains(nodelist,nodetree):
            if nodelist is None:
                return True
            if  (nodelist != None and nodetree is None):
                return False
            if nodelist.val != nodetree.val:
                if nodelist is  head :
                    return contains(head,nodetree.left) or contains(head,nodetree.right)
                else:
                    return contains(head,nodetree.left) or contains(head,nodetree.right) or contains(head,nodetree)
            
            x =  contains(nodelist.next,nodetree.right) or contains(nodelist.next, nodetree.left)
            if x:
                return True
            if nodelist is not head:
                return contains(head,nodetree)
            else:
                return False
        x =  contains(head,root)
        # print(x)
        # print(contains(head,root.right))
        return x