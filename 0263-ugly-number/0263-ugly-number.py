class Solution:
    def isUgly(self, n: int) -> bool:
        prev = 0
        while True:
            if n % 5 == 0:
                n //= 5
            elif n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            
            if n == 1:
                return True
            
            if n == prev:
                return False
            
            prev = n
            
        
            
            
            
                
            
            
        