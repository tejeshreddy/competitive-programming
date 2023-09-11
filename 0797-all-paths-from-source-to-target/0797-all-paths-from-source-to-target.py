class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        queue = [[0]]
        
        while queue:
            path = queue.pop(0)
            for neigh in graph[path[-1]]:
                temp = path.copy()
                temp.append(neigh)
                if temp[-1] == len(graph) - 1:
                    result.append(temp)
                else:
                    queue.append(temp)
        return result
                
        
        
        
        