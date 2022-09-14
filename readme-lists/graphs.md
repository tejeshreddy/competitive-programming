# Graphs

## Graph Questions

### Easy

- <https://leetcode.com/problems/employee-importance/>
- <https://leetcode.com/problems/find-the-town-judge/>

### Medium

- <https://leetcode.com/problems/evaluate-division/>
- <https://leetcode.com/problems/accounts-merge/>
- <https://leetcode.com/problems/network-delay-time/>
- <https://leetcode.com/problems/find-eventual-safe-states/>
- <https://leetcode.com/problems/keys-and-rooms/>
- <https://leetcode.com/problems/possible-bipartition/>
- <https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/>
- <https://leetcode.com/problems/regions-cut-by-slashes/>
- <https://leetcode.com/problems/satisfiability-of-equality-equations/>
- <https://leetcode.com/problems/as-far-from-land-as-possible/>
- <https://leetcode.com/problems/number-of-closed-islands/>
- <https://leetcode.com/problems/number-of-operations-to-make-network-connected/>
- <https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/>
- <https://leetcode.com/problems/time-needed-to-inform-all-employees/>

## BFS

### Medium

- <https://leetcode.com/problems/number-of-islands/>
- <https://leetcode.com/problems/rotting-oranges/>
- <https://leetcode.com/problems/snakes-and-ladders/>
- <https://leetcode.com/problems/is-graph-bipartite/>
- <https://leetcode.com/problems/minimum-jumps-to-reach-home/>

### Hard

- <https://leetcode.com/problems/word-ladder/>
- <https://leetcode.com/problems/word-ladder-ii/>
- <https://leetcode.com/problems/cut-off-trees-for-golf-event/>
- <https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/>

## DFS

### Medium

- <https://leetcode.com/problems/letter-combinations-of-a-phone-number/>
- <https://leetcode.com/problems/course-schedule-ii/>
- <https://leetcode.com/problems/decode-string/>
- <https://leetcode.com/problems/number-of-provinces/>
- <https://leetcode.com/problems/clone-graph/>
- <https://leetcode.com/problems/shortest-bridge/>
- <https://leetcode.com/problems/all-paths-from-source-to-target/>
This question is an all paths from source to destination problem
- <https://leetcode.com/problems/surrounded-regions//>
- <https://leetcode.com/problems/house-robber-iii/>

### Hard

- <https://leetcode.com/problems/critical-connections-in-a-network/>
- <https://leetcode.com/problems/remove-invalid-parentheses/>
- <https://leetcode.com/problems/longest-increasing-path-in-a-matrix/>
- <https://leetcode.com/problems/concatenated-words/>
- <https://leetcode.com/problems/making-a-large-island/>
- <https://leetcode.com/problems/contain-virus/>
- <https://leetcode.com/problems/24-game/>
- <https://leetcode.com/problems/remove-boxes/>

## Shortest Path Algorithms

### Dijkstra Algorith : Single source shortest path

<https://leetcode.com/problems/network-delay-time/>

The difference between any BFS and Dijkstra is that it uses a min heap

Using heaps gives us a logN operation to get the minimum length

Time Complexity:
Elog(V^2) = Elog(V)

Space Complexity:
O(V^2) If the edges are all bi-directional

```python
from typing import List
from collections import defaultdict
from heapq import heappush, heappop, heapify, heappushpop
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(int)

        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visited) == n else -1
```

## Minimum Spanning Tree

### Prims Algorithm

<https://leetcode.com/problems/min-cost-to-connect-all-points>

Space: O(V^2)

Time: O(E logV). It is O(n ^ 2 log n) where n is the total nodes and log n is the heap implementation

```python
from heapq import heappush, heappop
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        # Building the adjacency list
        adjlist = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs (y2 - y1)
                adjlist[i].append([dist, j])
                adjlist[j].append([dist, i])

        # Prim's Implementation
        minHeap = [[0, 0]] # [Weight, Node]
        visit = set()
        res = 0
        
        while len(visit) < N:
            w1, n1 = heappop(minHeap)
            if n1 in visit:
                continue
            res += w1
            visit.add(n1)
            
            for w2, n2 in adjlist[n1]:
                if n2 in visit:
                    continue
                heappush(minHeap, [w2, n2])
        
        return res
```

## Union Find

<https://leetcode.com/problems/redundant-connection/>

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            p = parent[n]
            while parent[p] != p:
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]

```

## Other Topics

### Number of Connected Components in an Undirected Graph

- <https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/>

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for neigh in graph[i]:
                dfs(neigh)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count    
```

'''text
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.

Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.

Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
'''

```python
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        result = float("+inf")
        rows, cols = len(grid), len(grid[0])
        person = None
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    person = [r, c]
                    break
            if person != None:
                break
        
        q = [(0, person)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        
        while q:
            dist, (x, y) = q.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if grid[x][y] == "#":
                result = min(result, dist)
                continue
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != "X":
                    q.append((dist + 1, [nx, ny]))
        if result != float("+inf"):
            return result
        return -1
```
