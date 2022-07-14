# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0, 0)
            ans, children, total = 0, 1, node.val
            for next_node in (node.left, node.right):
                result = dfs(next_node)
                ans += result[0]
                children += result[1]
                total += result[2]
                
            if total // children == node.val:
                ans += 1
            return (ans, children, total)
        return dfs(root)[0]