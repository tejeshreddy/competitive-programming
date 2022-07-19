class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        
        def dfs(u, v):
            if u not in visit:
                visit.add(u)
                if u == v:
                    return True
                return any(dfs(nei, v) for nei in graph[u])
                
        
        for u, v in edges:
            visit = set()
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        