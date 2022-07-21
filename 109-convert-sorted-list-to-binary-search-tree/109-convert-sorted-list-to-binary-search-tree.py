# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBST(self, values):
        if not values:
            return None
        l, r = 0, len(values) - 1
        mid = (l + r) // 2
        node = TreeNode(values[mid])
        node.left = self.createBST(values[:mid])
        node.right = self.createBST(values[mid + 1:])
        
        return node
    
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return self.createBST(values)
    
        
        
        