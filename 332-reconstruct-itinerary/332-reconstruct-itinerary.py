class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()
        for s, d in tickets:
            adj[s].append(d)
        
        result = ["JFK"]
        def dfs(src):
            if len(result) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            test = list(adj[src])
            for i, v in enumerate(test):
                adj[src].pop(i)
                result.append(v)
                
                if dfs(v):
                    return True
                
                adj[src].insert(i, v)
                result.pop()
            return False
        
        dfs("JFK")
        return result
                
                
                
            
        