class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            temp = target - n
            l, r = i + 1, len(numbers) - 1
            
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == temp:
                    return [i + 1, mid + 1]
                elif temp > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        
        