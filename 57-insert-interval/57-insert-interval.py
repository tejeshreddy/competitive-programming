class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        
        for i in intervals:
            if not result:
                result.append(i)
            else:
                if i[0] <= result[-1][1]:
                    result[-1][1] = max(result[-1][1],  i[1])
                else:
                    result.append(i)
        return result
        
        
        
        
        