class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        line = 0
        direction = 1
        
        output = [""] * numRows
        for char in s:
            output[line] += char
            
            if numRows > 1:
                line += direction
                if line == 0 or line == numRows - 1:
                    direction *= -1
        return "".join(output)
            
            
                
            
        