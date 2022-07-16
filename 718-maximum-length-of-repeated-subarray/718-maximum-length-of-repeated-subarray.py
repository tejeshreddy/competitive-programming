class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len_n1 = len(nums1)
        len_n2 = len(nums2)
        max_len = 0
        
        grid = [[0 for _ in range(len_n2 + 1)] for _ in range(len_n1 + 1)]
        
        for r in range(len_n1 - 1, -1, -1):
            for c in range(len_n2 - 1, -1, -1):
                if nums1[r] == nums2[c]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                    max_len = max(max_len, grid[r][c])
        return max_len
                    
        
        