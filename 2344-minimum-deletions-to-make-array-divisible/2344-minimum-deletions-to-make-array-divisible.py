class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = gcd(*numsDivide)
        nums = sorted(nums)
        
        for i, n in enumerate(nums):
            if g % n == 0:
                return i
            if n > g:
                break
        return -1
        
        
        