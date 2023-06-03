class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        adj = collections.defaultdict(list)
        for i in range(len(manager)):
            adj[manager[i]].append(i)
        
        queue = deque([(headID, 0)])
        result = 0
        while queue:
            i, time = queue.popleft()
            result = max(result, time)
            for neigh in adj[i]:
                queue.append((neigh, time + informTime[i]))
            
        return result