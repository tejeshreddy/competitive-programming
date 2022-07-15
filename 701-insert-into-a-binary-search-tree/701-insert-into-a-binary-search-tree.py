# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.nodes.append(root.val)
        self.inorder(root.right)
    
    def list_to_BST(self, nodes):
        
        if not nodes:
            return None
        
        mid = len(nodes) // 2
        root = TreeNode(nodes[mid])
        
        root.left = self.list_to_BST(nodes[:mid])
        root.right = self.list_to_BST(nodes[mid + 1:])
        
        return root
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.inorder(root)
        self.nodes += [val]
        
        return self.list_to_BST(sorted(self.nodes))
