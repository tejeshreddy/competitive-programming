class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans_0 = set(i for i in nums1 if i not in set(nums2))
        ans_1 = set(i for i in nums2 if i not in set(nums1))
        return [list(ans_0), list(ans_1)]
        