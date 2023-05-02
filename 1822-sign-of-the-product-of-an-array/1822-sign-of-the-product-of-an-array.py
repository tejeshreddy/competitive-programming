class Solution:
    def arraySign(self, nums: List[int]) -> int:
        zero = False
        negatives = 0
        for i in nums:
            if i < 0:
                negatives += 1
            if i == 0:
                zero = True
        if zero:
            return 0
        if negatives % 2 == 1:
            return -1
        return 1
        