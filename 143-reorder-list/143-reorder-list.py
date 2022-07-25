# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        
        l, r = 0, len(nodes) - 1
        cur = head
        
        while l <= r:
            cur.val = nodes[l]
            l += 1
            cur = cur.next
            
            if not cur:
                break
                
            cur.val = nodes[r]
            r -= 1
            cur = cur.next
            
            
        