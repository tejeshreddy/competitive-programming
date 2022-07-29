class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(int)
        for s, d in roads:
            graph[s] += 1
            graph[d] += 1
        
        graph = dict(sorted(graph.items(), key=lambda x: x[1], reverse=True))
        
        result = 0
        for k, v in graph.items():
            result += v * n
            n -= 1
        return result
        
        