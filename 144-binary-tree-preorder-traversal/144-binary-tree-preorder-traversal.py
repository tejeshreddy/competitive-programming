# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        cur = root
        while stack or cur:
            
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            
            cur = cur.right
        
        return result
        # if not root:
        #     return
        # self.result.append(root.val)
        # self.preorderTraversal(root.left)
        # self.preorderTraversal(root.right)
        # return self.result
        