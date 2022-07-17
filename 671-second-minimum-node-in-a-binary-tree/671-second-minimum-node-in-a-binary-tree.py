# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float("inf")
        min1 = root.val
        
        def dfs(node):
            
            if node:
                print(node.val)
                if min1 < node.val < self.ans:
                    self.ans = node.val
                if node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans < float("inf") else -1
        