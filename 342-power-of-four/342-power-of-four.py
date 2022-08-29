class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        print(n)
        if n == 1:
            return True
        if n <= 0:
            return False
        if n % 4 != 0:
            return False
        if n % 2 == 1:
            return False
        
        return self.isPowerOfFour(math.ceil(n // 4))