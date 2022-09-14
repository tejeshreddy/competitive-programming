class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = collections.Counter(tasks)
        heap = [-cnt for cnt in hmap.values()]
        heapq.heapify(heap)
        q = deque() #[cnt, time]
        time = 0
        print(heap)
        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
                
                
            
            
        
        
            