# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        high = head
        low = head
        
        while high != None and high.next != None :
            high = high.next.next
            low = low.next
            if high == low :
                return True
            
        
        return False
        