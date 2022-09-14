# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.left, self.right = None, None
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        
        if val > root.val:
            self.left = self.searchBST(root.right, val)
        else:
            self.right = self.searchBST(root.left, val)
        return self.left or self.right
        