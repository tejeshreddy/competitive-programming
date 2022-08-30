class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        q = [[0, 0]] # [Weight, Node]
        visited = set()
        total = 0
        
        while len(visited) != len(points):
            w, n = heapq.heappop(q)
            if n in visited:
                continue
            visited.add(n)
            total += w
            for w2, n2 in graph[n]:
                if n2 not in visited:
                    heapq.heappush(q, [w2, n2])
        return total
            
            
            
        
        
        
        
        
                
                
                