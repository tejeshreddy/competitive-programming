class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dic = {val: ind for ind, val in enumerate(arr)}
        dp = defaultdict(lambda: 2)
        
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] - arr[j] in dic and dic[arr[i] - arr[j]] < j:
                    k = dic[arr[i] - arr[j]]
                    dp[(i, j)] = 1 + dp[(j, k)]
        return max(dp.values()) if dp else 0
            
        