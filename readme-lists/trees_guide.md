
# Binary Tree

## Taking Input

### Using Stack

### Using Queue

## Binary Tree Traversals

### PreOrder

<https://leetcode.com/problems/binary-tree-preorder-traversal/>

Recursive Solution

Time: O(n)

Space: O(n) - Dependent on the call stack

```python
class Solution:
    def __init__(self):
        self.result = []
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.result
```

Iterative Solution

```python
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
```

### PostOrder

```python
class Solution:
    def __init__(self):
        self.result = []
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.result.append(root.val)
        return self.result
```

### InOrder

```python
class Solution:
    def __init__(self):
        self.result = []
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.postorderTraversal(root.left)
        self.result.append(root.val)
        self.postorderTraversal(root.right)
        return self.result
```

### Level Order

1. We put our root into queue, now we have level 0 in our queue.
2. On each step extract all nodes from queue and put their children to to opposite end of queue. In this way we will have full level in the end of each step and our queue will be filled with nodes from the next level.
3. In the end we just return result.

Complexity: Time complexity is O(n): we perform one bfs on our tree. Space complexity is also O(n), because we have answer of this size.

```python
class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, result = deque([root]), []
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
        return result
```

### Boundry Traversal

```python
class Solution:
    def __init__(self):
        self.result = []

    def left_view(self, node):
        if not node:
            return
        if not node.left and not node.right:
            return
        self.result.append(node.val)
        if node.left:
            self.left_view(node.left)
        else:
            self.left_view(node.right)
        
    def right_view(self, node):
        if not node:
            return
        if not node.left and not node.right:
            return
        if node.right:
            self.right_view(node.right)
        else:
            self.right_view(node.left)
        self.result.append(node.val)
        
    def leaf_node(self, node):
        if not node:
            return
        if not node.left and not node.right:
            self.result.append(node.val)
        self.leaf_node(node.left)
        self.leaf_node(node.right)
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.result.append(root.val)
        if root.left != None or root.right != None:
            
            self.left_view(root.left)
            self.leaf_node(root)
            self.right_view(root.right)
        
        return self.result
```

### ZigZag Traversal

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return None
        queue = [root]
        side = False
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if side:
                result.append(level[::-1])
                side = False
            else:
                result.append(level)
                side = True
        return result
```

## Basic Questions

- Height of Binary Tree
- Diameter of Binary Tree
- Replace Node with Width
- 
