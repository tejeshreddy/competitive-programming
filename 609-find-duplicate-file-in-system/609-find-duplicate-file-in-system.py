class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for p in paths:
            info = p.split(" ")
            for c in info[1:]:
                c = c.replace(")", "").split("(")
                hmap[c[1]].append(info[0] +"/"+ c[0])
        
        result = []
        for k, v in hmap.items():
            if len(v) >= 2:
                result.append(v)
        return result
                
                
        