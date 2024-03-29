# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        
        def dfs(root):
            if not root:
                return 0
            left_sum = max(dfs(root.left), 0)
            right_sum = max(dfs(root.right), 0)
            
            self.result  = max(self.result, root.val + left_sum + right_sum)
            return root.val + max(left_sum, right_sum)
        
        dfs(root)
        return self.result
            