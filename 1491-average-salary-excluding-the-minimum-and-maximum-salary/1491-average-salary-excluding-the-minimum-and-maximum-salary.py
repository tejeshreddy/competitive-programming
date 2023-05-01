class Solution:
    def average(self, salary: List[int]) -> float:
        result = sum(salary) - min(salary) - max(salary)
        result = result / (len(salary) - 2)
        return round(result, 5)
        