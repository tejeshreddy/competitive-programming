# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(0, head)
        
        while head:
            count += 1
            head = head.next
        count = (count // 2)
        dummy = dummy.next
        
        while dummy:
            if count == 0:
                return dummy
            else:
                dummy = dummy.next
                count -= 1
        
            
        