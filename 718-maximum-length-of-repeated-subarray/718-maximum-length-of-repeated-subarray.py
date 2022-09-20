class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        grid = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        result = 0
        
        for r in range(len1 - 1, -1, -1):
            for c in range(len2 - 1, -1, -1):
                if nums1[r] == nums2[c]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                # else:
                #     grid[r][c] = max(grid[r + 1][c], grid[r][c + 1])
                result = max(grid[r][c], result)
        return result
                
                    
                    
        
        
        