class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 == 1: 
            return False
        lookup = collections.defaultdict(int)
        count = 0
        for i, num in enumerate(arr):
            key = k - (num % k)
            if key in lookup and lookup[key] >= 1:
                # print(key, num)
                count += 1
                lookup[key] -= 1
            else:
                lookup[(num % k) or k] += 1
        return count == len(arr) // 2
            
                
        