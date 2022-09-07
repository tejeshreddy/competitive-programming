class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        result = 0
        prev_end = intervals[0][1]
        
        
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                result += 1
                prev_end = min(prev_end, end)
        return result
                
                