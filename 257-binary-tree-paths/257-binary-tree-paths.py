# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    
    def dfs(self, root, values):
        if not root:
            return
        values.append(str(root.val))
        
        if root.left == None and root.right == None:
            self.result.append(values.copy())
        
        self.dfs(root.left, values)
        self.dfs(root.right, values)
        values.pop()
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.dfs(root, [])
        paths = []
        for p in self.result:
            paths.append("->".join(p))
        return paths
        