# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    
    def inorder_traversal(self, node) -> None:
        if not node:
            return
        self.inorder_traversal(node.left)
        self.nodes.append(node.val)
        self.inorder_traversal(node.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder_traversal(root)
        
        # Edge case and prevent out of bound error
        if len(self.nodes) == 1:
            return True
        
        for i in range(1, len(self.nodes)):
            if self.nodes[i] <= self.nodes[i - 1]:
                return False
        return True
        