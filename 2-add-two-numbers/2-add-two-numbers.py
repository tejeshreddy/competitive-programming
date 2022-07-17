# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        current = dummy = ListNode(0)
        carry = 0
        
        while l1 or l2:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry, remainder = divmod(total, 10)
            
            current.next = ListNode(remainder)
            current = current.next
        
        if carry:
            current.next = ListNode(carry)
        return dummy.next
        
        