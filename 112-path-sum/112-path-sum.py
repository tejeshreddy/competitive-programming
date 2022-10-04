# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, total):
            if not root:
                return False
            if not root.left and not root.right:
                if total - root.val == 0:
                    return True
                else:
                    return False
            
            return dfs(root.left, total - root.val) or dfs(root.right, total - root.val)
        
        return dfs(root, targetSum)
            