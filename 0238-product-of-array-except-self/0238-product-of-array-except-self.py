class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc = 0
        pc = 1
        
        for n in nums:
            if n == 0:
                zc += 1
            else:
                pc *= n
        result = []
        if zc == 0:
            for n in nums:
                result.append(pc // n)
        elif zc == 1:
            for n in nums:
                if n != 0:
                    result.append(0)
                else:
                    result.append(pc)
        else:
            result = [0] * len(nums)
        return result