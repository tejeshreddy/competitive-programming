class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = collections.Counter(arr)
        return len(list(hmap.values())) == len(set(hmap.values()))
        