# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = [root]
        result = []
        
        if root == None:
            return result
        
        while q:
            level = []
            next_q = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            result.append(level)
            q = next_q.copy()
            next_q = []
        return result
        
                
                
                
            
            
        
        