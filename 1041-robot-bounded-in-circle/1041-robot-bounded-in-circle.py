class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1
        x, y = 0, 0
        
        for direction in instructions:
            if direction == "G":
                x, y = x + dirX, y + dirY
            elif direction == "L":
                dirX, dirY = -1 * dirY, dirX
            else:
                dirX, dirY = dirY, -1 * dirX
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)
        
        
        