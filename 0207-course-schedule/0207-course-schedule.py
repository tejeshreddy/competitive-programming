class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = collections.defaultdict(list)
        visited = set()
        
        for a, b in prerequisites:
            hmap[b].append(a)
        
        def dfs(n):
            if hmap[n] == []:
                return True
            if n in visited:
                return False
            
            visited.add(n)
            for neigh in hmap[n]:
                if not dfs(neigh):
                    return False
                visited.add(neigh)
            hmap[n] = []
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True