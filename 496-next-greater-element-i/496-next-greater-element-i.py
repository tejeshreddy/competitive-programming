class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hmap = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                hmap[stack.pop()] = num
            stack.append(num)
        
        return [hmap.get(num, -1) for num in nums1]
            
        
        