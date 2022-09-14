class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        count = len(isConnected)
        result = 0
        visited = set()
        
        for k in range(count):
            if k in visited:
                continue
            
            q = [k]
            
            result += 1
            
            while q:
                node = q.pop(0)
                visited.add(node)
                
                for i, neigh in enumerate(isConnected[node]):
                    if neigh and i not in visited:
                        q.append(i)
        return result
                        
                        
                
            
            
            
            
        