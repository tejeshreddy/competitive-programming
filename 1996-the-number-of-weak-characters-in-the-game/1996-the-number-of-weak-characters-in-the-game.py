class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key = lambda x: (-x[0], x[1]))
        
        temp_max = 0
        result = 0
        
        for a, d in properties:
            if d < temp_max:
                result += 1
            else:
                temp_max = d
        return result
                
                
            
        
        
        
        