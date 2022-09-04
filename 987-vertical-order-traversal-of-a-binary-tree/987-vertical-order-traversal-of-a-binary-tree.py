# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = collections.defaultdict(list)
        q = [(root, 0)]
        
        while q:
            next_level = []
            hmap = collections.defaultdict(list)
            for node, s in q:
                hmap[s].append(node.val)
                if node.left:
                    next_level.append((node.left, s - 1))
                if node.right:
                    next_level.append((node.right, s + 1))
            for i in hmap:
                levels[i].extend(sorted(hmap[i]))
            q = next_level
        return [levels[i] for i in sorted(levels)]
