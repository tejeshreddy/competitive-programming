class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = "".join([c.lower() if c.isalnum() else " " for c in paragraph])
        banned = set(banned)
        hmap = {}
        for word in paragraph.split(" "):
            hmap[word] = hmap.get(word, 0) + 1
        print(hmap)
        hmap = sorted(hmap.items(), key=lambda x: (-x[1]))
        for k, v in hmap:
            if k not in banned and k != "":
                return k
        
        
        
        
        
        