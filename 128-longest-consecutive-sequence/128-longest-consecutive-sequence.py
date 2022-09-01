class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        for n in nums:
            if n + 1 not in nums:
                pointer = n
                count = 0
                while pointer in nums:
                    pointer = pointer - 1
                    count += 1
                result = max(result, count)
            else:
                continue
        return result
            