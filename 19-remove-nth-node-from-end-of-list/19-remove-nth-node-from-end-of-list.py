# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        count = 0
        
        while head:
            count += 1
            head = head.next
        count = count - n
        head = dummy
        
        while count > 0:
            head = head.next
            count -= 1
        head.next = head.next.next
        
        return dummy.next
            
        
        