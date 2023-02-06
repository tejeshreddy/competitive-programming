class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = len(nums) // 2
        
        result = []
        while j < len(nums):
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j += 1
        return result
        