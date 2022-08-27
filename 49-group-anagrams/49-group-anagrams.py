class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        hmap = collections.defaultdict(list)
        
        for word in strs:
            mapping = [0] * 26
            for c in word:
                mapping[ord(c) - ord("a")] += 1
            mapping = ["0" * (2 - len(str(i))) + str(i) for i in mapping]
            hmap["".join(mapping)].append(word)
        return list(hmap.values())
        
        
        