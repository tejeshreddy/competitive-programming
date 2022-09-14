class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        H = sorted([0] + horizontalCuts + [h])
        V = sorted([0] + verticalCuts + [w])
        max_h, max_v = 0, 0
        
        for i in range(1, len(H)):
            max_h = max(max_h, H[i] - H[i - 1])
        
        for i in range(1, len(V)):
            max_v = max(max_v, V[i] - V[i - 1])
        
        return (max_h * max_v) % (10 ** 9 + 7)
            
        
        
        # H = sorted([0] + horizontalCuts + [h])
        # V = sorted([0] + verticalCuts + [w])
        # return max(j-i for i,j in zip(H, H[1:])) * max(j-i for i,j in zip(V, V[1:])) % (10**9 + 7)
        