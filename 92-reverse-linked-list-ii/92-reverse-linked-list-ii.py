# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        newHead = head
        if not head:
            return head
        
        i = 0
        curr = None
        while i != left-1:
            curr  = head
            head = head.next
            i += 1
        leftNode = head
        now = None
        prev  = None
        while i != right  and head!= None :
            now = head
            head = head.next
            now.next = prev
            i += 1
            prev = now
        if curr != None:
            curr.next = now
        print(now)
        leftNode.next = head

        if left == 1 :
            return now
        return newHead