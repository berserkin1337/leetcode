# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        node = head
        while node != None :
            node = node.next
            length += 1
        prev = None 
        cur = head
        for i in range(length//2) :
            nx = cur.next
            cur.next= prev
            prev = cur
            cur = nx
            
        node1 = prev
        node2 = cur
        ans = 0
        while node1 != None :
            # print(node1.val,node2.val)
            ans = max(node1.val + node2.val , ans)
            node1 = node1.next
            node2 = node2.next
        return ans