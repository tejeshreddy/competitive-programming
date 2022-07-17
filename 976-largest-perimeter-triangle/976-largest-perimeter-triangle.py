class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        A = nums
        A.sort()
        # for i in range(len(nums) - 3):
        #     if nums[i] > nums[i + 1] + nums[i + 2]:
        #         return nums[i] + nums[i + 1] + nums[i + 2]
        # return 0
        for i in range(len(A) - 3, -1, -1):

            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
        