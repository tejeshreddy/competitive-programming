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

Time: O(E logV)

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
