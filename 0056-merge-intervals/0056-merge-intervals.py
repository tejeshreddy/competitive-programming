class Solution:
    def merge(self, intervals: List[List[int]] = []) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        
        for start, end in intervals:
            if not result:
                result.append([start, end])
            else:
                if result[-1][0] <= start <= result[-1][1]:
                    prev_start, prev_end = result.pop()
                    result.append([min(start, prev_start), max(end, prev_end)])
                else:
                    result.append([start, end])
        return result
                    
                    
                
                
        
        