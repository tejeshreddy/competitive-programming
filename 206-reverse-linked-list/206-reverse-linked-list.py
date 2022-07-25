# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = None
        cur = head
        nxt = cur.next
        
        while nxt:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = nxt.next
        cur.next = prev
        return cur
            
        
        