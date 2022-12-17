class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            hmap["".join(sorted_word)].append(word)
        return hmap.values()
        
        