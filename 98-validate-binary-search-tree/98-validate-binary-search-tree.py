# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def depth_first_search(self, node, low, high) -> bool:
        if not node:
            return True
        
        if low < node.val < high:
            return self.depth_first_search(node.left, low, node.val) and self.depth_first_search(node.right, node.val, high)
        else:
            return False
        
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.depth_first_search(root, float("-inf"), float("+inf"))
        