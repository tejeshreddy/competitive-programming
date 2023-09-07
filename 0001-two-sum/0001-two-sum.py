class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        9 - 2: 7 -> 0
        7 is in hmap, exit index(7), current index
        """
        hmap = {}
        
        for i, n in enumerate(nums):
            if n in hmap:
                return [hmap[n], i]
            else:
                hmap[target - n] = i
        
                
            
            
        
    
            
        