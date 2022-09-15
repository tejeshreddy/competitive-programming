# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        
        def dfs(root, total):
            if not root:
                return
            
                
            dfs(root.left, total - root.val)
            dfs(root.right, total - root.val)
            if total - root.val == 0:
                self.result += 1
                
        
        def inorder(root):
            if not root:
                return
            dfs(root, targetSum)
            
            inorder(root.left)
            inorder(root.right)
        
        inorder(root)
        return self.result
        
        
        
        