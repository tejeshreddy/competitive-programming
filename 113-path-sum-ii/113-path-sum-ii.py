# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    
    def dfs(self, root, values, targetSum):
        if not root:
            return
        
        values.append(root.val)
        
        if root.left == None and root.right == None and sum(values) == targetSum:
            self.result.append(values.copy())
            
        self.dfs(root.left, values, targetSum)
        self.dfs(root.right, values, targetSum)
        values.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.dfs(root, [], targetSum)
        return self.result
