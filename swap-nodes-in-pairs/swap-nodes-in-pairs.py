# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None :
            return head
        
        nx = head.next
        head.next = nx.next
        nx.next = head
        prev = head
        cur = head.next
        head = nx
        while  cur != None and cur.next != None :
            nx = cur.next
            cur.next = nx.next
            nx.next = cur
            prev.next = nx
            prev = cur
            cur = cur.next
        return head
            