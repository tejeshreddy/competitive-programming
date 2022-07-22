# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        left = ListNode(0, None)
        right = ListNode(0, None)
        
        dummyl = ListNode(0, left)
        dummyl = dummyl.next
        
        dummyr = ListNode(0, right)
        dummyr = dummyr.next
        
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        
        right.next = None
        left.next = None
        left.next = dummyr.next
            
        return dummyl.next