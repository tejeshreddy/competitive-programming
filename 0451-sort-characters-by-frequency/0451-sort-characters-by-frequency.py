class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = collections.Counter(s)
        hmap = sorted(hmap.items(), key=lambda x: (-x[1]))
        
        result = ''
        while hmap:
            s, c = hmap.pop(0)
            result += s * c
        return result
        