class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap_ransom = {}
        hmap_magazine = {}
        
        for i in ransomNote:
            hmap_ransom[i] = hmap_ransom.get(i, 0) + 1
        
        for i in magazine:
            hmap_magazine[i] = hmap_magazine.get(i, 0) + 1
        
        for k, v in hmap_ransom.items():
            if k not in hmap_magazine:
                return False
            if v > hmap_magazine[k]:
                return False
        return True
                
        