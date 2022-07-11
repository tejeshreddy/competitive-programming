
"""
https://leetcode.com/problems/network-delay-time/
Dijkstra Algorith: Single source shortest path

The difference between any BFS and Dijkstra is that it uses a min heap

Using heaps gives us a logN operation to get the minimum length

Time Complexity:
Elog(V^2) = Elog(V)

Space Complexity:
O(V^2) If the edges are all bi-directional
"""
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

