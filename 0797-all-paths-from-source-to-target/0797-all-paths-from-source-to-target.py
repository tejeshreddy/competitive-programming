class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        queue = [[0]]
        
        while queue:
            path = queue.pop(0)
            for neigh in graph[path[-1]]:
                if neigh == len(graph) - 1:
                    result.append(path + [neigh])
                else:
                    queue.append(path + [neigh])
        return result
                
        
        
        
        