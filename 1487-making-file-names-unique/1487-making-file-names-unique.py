class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used, hmap = set(), collections.defaultdict(int)
        result = []

        for name in names:
            k = hmap[name]
            current = name
            print(current)
            while current in used:
                k += 1
                current = "%s(%d)" % (name, k)

            hmap[name] = k
            result.append(current)
            used.add(current)
        return result