class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        rotation = l
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            rmid = (mid + rotation) % len(nums)
            if nums[rmid] == target:
                return rmid
            if target > nums[rmid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
                
        
        
        
#         zi = nums.index(0)
#         nums = nums[zi:] + nums[:zi]
        
#         l, r = 0, len(nums)
        
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return (mid + zi) % len(nums)
            
#             if target < nums[mid]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return -1

