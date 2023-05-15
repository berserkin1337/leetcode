# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        backonek = None
        onek = head
        for i in range(k-1):
            backonek = onek
            onek = onek.next
        twok = head
        backtwok = None
        node = onek
        while node.next != None :
            node = node.next
            backtwok = twok
            twok = twok.next
        print(onek.val)
        print(twok.val)       
        # frontonek = onek.next
        # fronttwok = twok.next
        # backonek.next = twok
        # if frontonek != twok :
        #     twok.next = frontonek
        # backtwok.next = onek
        # if fronttwok != onek:
        #     onek.next= fronttwok
        onek.val , twok.val = twok.val,onek.val
        return head

