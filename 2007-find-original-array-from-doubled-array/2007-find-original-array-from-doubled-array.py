class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        hmap = Counter(changed)
        
        result = []
        changed.sort()
        
        for n in changed:
            if n == 0 and hmap[0] >= 2:
                print(n)
                result.append(0)
                hmap[0] -= 2
            elif n != 0 and hmap[n] and hmap[n * 2]:
                result.append(n)
                hmap[n] -= 1
                hmap[n * 2] -= 1
        
        if len(result) == len(changed) // 2:
            return result
        return []