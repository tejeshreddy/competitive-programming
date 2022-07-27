class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        result = [0] * (n + 1)
        hmap = collections.defaultdict(list)
        
        for t in trust:
            hmap[t[1]].append(t[0])
            result[t[0]] += 1
        
        
        for k, v in enumerate(result):
            if v == 0 and k != 0 and len(hmap[k]) == n - 1:
                return k

        return -1
        