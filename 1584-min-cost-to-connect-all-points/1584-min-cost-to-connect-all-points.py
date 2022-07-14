class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        hmap = collections.defaultdict(list)
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                hmap[i].append([dist, j])
                hmap[j].append([dist, i])
        visited = set()
        cost = 0
        
        q = [[0, 0]]
        while len(visited) != N:
            dist, node = heapq.heappop(q)
            if node not in visited:
                cost += dist
                visited.add(node)
                for neigh in hmap[node]:
                    if neigh[1] not in visited:
                        heapq.heappush(q, neigh)
        return cost
                
                
        
        
        
        
                
                
        
        
        
        