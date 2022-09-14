class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = {i: 0 for i in range(10)}
        
        def dfs(node, count):
            if not node.left and not node.right:
                odd = 1
                for key in count:
                    if count[key] % 2 != 0:
                        if odd: odd -= 1
                        else: return 0
                return 1
            
            result = 0
            if node.left:
                count[node.left.val] += 1
                result += dfs(node.left, count)
                count[node.left.val] -= 1
            if node.right:
                count[node.right.val] += 1
                result += dfs(node.right, count)
                count[node.right.val] -= 1
            return result
        
        count[root.val] = 1
        return dfs(root, count)