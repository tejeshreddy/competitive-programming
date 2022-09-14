class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}
        result = []
        
        for i, c in enumerate(s):
            hmap[c] = i
        anchor = 0
        for i, c in enumerate(s):
            anchor = max(anchor, hmap[c])
            if anchor == i:
                if not result:
                    result.append(i + 1)
                    continue
                result.append((i + 1) - sum(result))
        return result
            