# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.result = 0
        
        def dfs(root, temp_max):
            if not root:
                return
            if root.val >= temp_max:
                self.result += 1
            dfs(root.left, max(root.val, temp_max))
            dfs(root.right, max(root.val, temp_max))
        
        dfs(root, float("-inf"))
        return self.result
            
        