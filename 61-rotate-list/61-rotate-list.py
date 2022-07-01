# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None :
            return head
        elif head.next == None:
            return head
        size = 0 
        tmp = head
        
        while tmp != None:
            size += 1
            tmp  = tmp.next
        k = k %size
        # rotating the list to the right by k  is equivalent to 
        #rotating the list to the left by  size - k
        
        k = size - k
        # print(k)
        num = 0
        right = head
        nums = []
        while num != k :
            num +=  1
            nums.append(right.val)
            # print(right.val)
            right = right.next
        
        left = head
        
        while right != None :
            left.val = right.val
            right = right.next
            left = left.next
        
        i = 0
        while i < len(nums) and left != None :
            left.val = nums[i]
            left = left.next
            i += 1
        # print(nums)
        return head