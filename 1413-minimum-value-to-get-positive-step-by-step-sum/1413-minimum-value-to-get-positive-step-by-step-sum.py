class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        startValue = 1
        
        while True:
            temp = startValue
            result = []
            for value in nums:
                temp = temp + value
                result.append(temp)
            
            bool_result = [i >= 1 for i in result]
            if all(bool_result):
                return startValue
            startValue += 1
            
            
        
        