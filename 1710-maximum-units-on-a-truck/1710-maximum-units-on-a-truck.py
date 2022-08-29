class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        
        result = 0
        
        for count, units in boxTypes:
            if count <= truckSize:
                truckSize -= count
                result += count * units
            elif truckSize > 0:
                result += truckSize * units
                truckSize = 0
            elif truckSize == 0:
                break
                
        return result
                
                