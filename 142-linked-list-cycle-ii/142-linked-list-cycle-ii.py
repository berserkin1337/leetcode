# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        # print("hi")
        while fast != None and fast.next != None :
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break
        # print(fast)
        if fast is None or fast.next is None:
            return None
        # print("hi")
        while head != slow:
            head = head.next
            slow = slow.next
            print(head.val)
        return head