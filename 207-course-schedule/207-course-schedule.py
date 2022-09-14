class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = set()
        
        def dfs(node):
            if graph[node] == []:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
                visited.add(neigh)
            graph[node] = []
            return True
            
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
        
        