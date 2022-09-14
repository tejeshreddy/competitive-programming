class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc  = 0
        prod = 1
        
        for n in nums:
            if n != 0:
                prod *= n
            elif n == 0:
                zc += 1
        result = []
        if zc > 1:
            return [0] * len(nums)
        elif zc == 1:
            for n in nums:
                if n == 0:
                    result.append(prod)
                else:
                    result.append(0)
            return result
        elif zc == 0:
            for n in nums:
                result.append(prod // n)
            return result
            
            
        