class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False
        if len(start) != len(target):
            return False
        N = len(start)
        i, j = 0, 0
        while i < N and j < N:
            while i < N and start[i] == "_":
                i += 1
            while j < N and target[j] == "_":
                j += 1
            while i < N and j < N and ((start[i] == "L" and i < j) or (start[i] == "R" and i > j)):
                return False
            i += 1
            j += 1
        return True
            
        