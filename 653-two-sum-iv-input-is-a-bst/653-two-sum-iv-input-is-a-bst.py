# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        values = []
        def dfs(root):
            if not root:
                return
            values.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        twosum = []
        
        for i in values:
            if i in twosum:
                return True
            twosum.append(k - i)
        return False
            
        