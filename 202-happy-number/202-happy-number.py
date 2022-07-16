class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        while n not in visited and n != 1:
            visited.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1
        