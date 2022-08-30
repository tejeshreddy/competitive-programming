class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        hmap = collections.defaultdict(list)
        
        for u, v, w in times:
            hmap[u].append((v, w))
        
        min_heap = [(0, k)]
        t = 0
        
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            
            for n2, w2 in hmap[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w2 + w1, n2))
        return t if len(visited) == n else -1
                
                
        
        
        
            
        