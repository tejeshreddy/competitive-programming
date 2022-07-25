# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
    
        def checkSame(root, subRoot):
            if not root and not subRoot:
                return True

            if (not root and subRoot) or (not subRoot and root):
                return False

            if root.val != subRoot.val:
                return False

            return checkSame(root.left, subRoot.left) and checkSame(root.right, subRoot.right)
        
        
    
        def dfs(root):
            if not root:
                return False

            if root.val == subRoot.val:
                if checkSame(root, subRoot):
                    return True
            return dfs(root.left) or dfs(root.right)
        
        
        return dfs(root)
    
    
    
    
    
    