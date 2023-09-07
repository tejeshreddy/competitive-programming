class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        
        """
        hmap = collections.defaultdict(list)
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            hmap[sorted_s].append(s)
        return list(hmap.values())
            
        