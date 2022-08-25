# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curnode = dummy = ListNode(0)
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
            curnode.next = ListNode(remainder)
            curnode = curnode.next
        if carry:
            curnode.next = ListNode(carry)
        
        return dummy.next
            
        
        