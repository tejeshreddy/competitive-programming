class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while True:
            if n == 3 ** i:
                return True
            elif n < 3 ** i:
                return False
            i += 1
        