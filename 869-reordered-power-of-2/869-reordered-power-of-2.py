class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(n)))
            
        