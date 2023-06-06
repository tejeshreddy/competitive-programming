class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        
        arr.sort()
        diff = abs(arr[0] - arr[1])
        
        for i in range(2, len(arr)):
            if diff != abs(arr[i] - arr[i - 1]):
                return False
    
        return True
        