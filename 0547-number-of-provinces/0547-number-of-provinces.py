class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        
        for i in range(len(isConnected)):
            for k, v in enumerate(isConnected[i]):
                if v == 1:
                    graph[i].append(k)
        
        visited = set()
        
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for neigh in graph[i]:
                if neigh not in visited:
                    dfs(neigh)
        
        comps = 0
        for n in range(len(isConnected)):
            if n not in visited:
                comps += 1
                dfs(n)
        return comps
                
            
            
        
        