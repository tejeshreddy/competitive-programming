class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        N = len(points)
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        
        queue = [(0, 0)]
        visited = set()
        result = 0
        
        while len(visited) != N:
            w1, p1 = heapq.heappop(queue)
            if p1 not in visited:
                result += w1
                visited.add(p1)
            
            for points in graph[p1]:
                w2, p2 = points
                if p2 not in visited:
                    heapq.heappush(queue, (w2, p2))
                
        return result
            
                
                
            