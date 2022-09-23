class Solution:
    def concatenatedBinary(self, n: int) -> int:
        resulting_string = ""
        MOD = 10 ** 9 + 7
        total = 0
        
        for i in range(1, n+1):
            resulting_string += bin(i)[2:]
        return int(resulting_string, 2) % MOD
        
        