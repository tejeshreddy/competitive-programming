class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " " + s2
        hmap = collections.Counter(s.split(" "))
        result = []
        for k, v in hmap.items():
            if v == 1:
                result.append(k)
        return result