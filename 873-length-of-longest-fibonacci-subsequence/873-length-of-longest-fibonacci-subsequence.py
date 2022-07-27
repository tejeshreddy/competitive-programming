class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        result = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                x, y = arr[j], arr[i] + arr[j]
                length = 2
                
                while y in s:
                    x, y = y, x + y
                    length += 1
                result = max(result, length)
        return result if result >= 3 else 0
                
        
#         dic = {val: ind for ind, val in enumerate(arr)}
#         dp = defaultdict(lambda: 2)
        
#         for i in range(len(arr)):
#             for j in range(i):
#                 if arr[i] - arr[j] in dic and dic[arr[i] - arr[j]] < j:
#                     k = dic[arr[i] - arr[j]]
#                     dp[(i, j)] = 1 + dp[(j, k)]
#         return max(dp.values()) if dp else 0


            
        