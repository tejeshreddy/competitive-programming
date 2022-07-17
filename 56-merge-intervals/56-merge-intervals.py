class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        
        result = [intervals.pop(0)]
        
        while intervals:
            recent = intervals.pop(0)
            
            if recent[0] <= result[-1][1]:
                result[-1][1] = max(recent[1], result[-1][1])
                # merge = result.pop()
                # recent = [min(recent[0], merge[0]), max(recent[1], merge[1])]
            else:
                result.append(recent)
        return result
        
        
        