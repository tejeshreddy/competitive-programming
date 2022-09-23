class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = [str(i) for i in range(1, 10)]
        result = []
        
        while q:
            r = q.pop(0)
            if len(r) == n:
                result.append(r)
                continue
            p = int(r[-1])
            
            if p + k < 10:
                q.append(r + str(p + k))
            if p - k >= 0:
                q.append(r + str(p - k))
        return list(set(result))
                
            
            
        