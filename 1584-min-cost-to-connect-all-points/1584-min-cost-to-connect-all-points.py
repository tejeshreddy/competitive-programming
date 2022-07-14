from heapq import heappush, heappop

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
            
        
        