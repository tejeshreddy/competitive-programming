class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        return n.count("1")
        