
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

### Height of Binary Tree

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

Space: O(n) Recursive call stack
Time: O(n)

### Diameter of Binary Tree

```python
class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(left + right, self.diameter)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter
```

Space: O(n) - Recursive call stack
Time: O(n)

### Replace Node with Width

### LCA Of Binary  Tree

## Construction Of Trees

### Binary Tree From PreOrder And InOrder

### Binary Tree From Parent Array

## Tree Views

### Top View

### Left View

### Right View

### Bottom View

# Binary Search Tree

- <https://www.freecodecamp.org/news/binary-search-trees-bst-explained-with-examples/>
- The way that they are set up means that, on average, each comparison allows the operations to skip about half of the tree, so that each lookup, insertion or deletion takes time proportional to the logarithm of the number of items stored in the tree,  O(log n).
- Some times the worst case can happen, when the tree isn't balanced and the time complexity is  O(n)  for all three of these functions. That is why self-balancing trees (AVL, red-black, etc.) are a lot more effective than the basic BST.

- Time Complexity for searching (DFS and BFS), deleting and inserting: O(h)

-

## Search, Insertion and Delete in BST

### Search BST

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
```

### Insertion BST

- Longer Approach: Getting the array, adding the element, sorting the array. And, then dividing the array into parts and recursively passing to the function to build BST from array

```python
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
```

- Shorter Approach

```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root
```

### Validate BST

<https://leetcode.com/problems/validate-binary-search-tree/>

```python
class Solution:
    def __init__(self):
        self.nodes = []
    
    def inorder_traversal(self, node) -> None:
        if not node:
            return
        self.inorder_traversal(node.left)
        self.nodes.append(node.val)
        self.inorder_traversal(node.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder_traversal(root)
        
        # Edge case and prevent out of bound error
        if len(self.nodes) == 1:
            return True
        
        for i in range(1, len(self.nodes)):
            if self.nodes[i] <= self.nodes[i - 1]:
                return False
        return True
```

DFS Approach

```python
class Solution:
    
    def depth_first_search(self, node, low, high) -> bool:
        if not node:
            return True
        
        if low < node.val < high:
            return self.depth_first_search(node.left, low, node.val) and self.depth_first_search(node.right, node.val, high)
        else:
            return False
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.depth_first_search(root, float("-inf"), float("+inf"))
```

## Construction of BST

### Construct BST From LevelOrder

### Construct BST From Keys 1 to N

## Conversion Based Problems

### Binary Tree To BST

### Sorted Linked List To Balanced BST

### Convert BST To Min Heap

## Modification in BSTs

### Merge Two BST

### Fix BST

## Standard Problems

### LCA in BST

### Pair Sum in BST

### Kth Largest Number In BST

## Segment Tree

## Fenwick Tree
