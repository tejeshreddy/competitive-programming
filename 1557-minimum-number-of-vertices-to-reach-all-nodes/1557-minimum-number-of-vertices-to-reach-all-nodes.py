class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hmap = collections.defaultdict(list)
        in_degree = [0] * n
        
        for s, d in edges:
            hmap[s].append(d)
            in_degree[d] += 1
        
        return [i for i in range(len(in_degree)) if in_degree[i] == 0]
        
        
        