class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        all elements are positivie -> [1, 2, 3, 4] => 24 => [24, 12, 8, 6]
        negatives -> [-2, -3, 5, 6] -> 180 -> [-90, -60, 36, 30]
        zeros -> [0, 2, 3, 4] -> [24, 0, 0, 0]
        multiple zeros => [0, 2, 0, 3] -> [0, 0, 0, 0]
        
        1. count the number of 0's
        2. if zero count gt 2
            steps
        3 if zero count lt 2 gt 0
            steps
        4. normal steps
        """
        zero_count = 0
        product = 1
        
        for number in nums:
            if number == 0:
                zero_count += 1
            else:
                product *= number
        
        result = []
        
        if zero_count > 0:
            if zero_count >= 2:
                result = [0] * len(nums)
            else:
                for number in nums:
                    if number == 0:
                        result.append(product)
                    else:
                        result.append(0)
        else:
            for number in nums:
                result.append(int(product/number))
        
        return result
            
        
                
            
        