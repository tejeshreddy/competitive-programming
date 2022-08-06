class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        cur_count, cur_grades = 0, 0
        prev_count, prev_grades = 0, 0
        result = 0
        
        for grade in grades:
            cur_grades += grade
            cur_count += 1
            
            if cur_grades > prev_grades and cur_count > prev_count:
                result += 1
                
                prev_grades, prev_count = cur_grades, cur_count
                cur_count, cur_grades = 0, 0
        return result