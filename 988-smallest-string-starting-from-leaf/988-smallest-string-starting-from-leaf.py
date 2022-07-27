# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []
    
    def dfs(self, root, value):
        if not root:
            return
        value.append(chr(root.val + ord("a")))
        
        if root.left == None and root.right == None:
            self.paths.append(value.copy())
        
        self.dfs(root.left, value)
        self.dfs(root.right, value)
        value.pop()
        
    
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.dfs(root, [])
        concat_paths = []
        
        for p in self.paths:
            concat_paths.append("".join(p[::-1]))
        return sorted(concat_paths)[0]
        