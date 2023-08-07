class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        element_row = []
        for i in matrix:
            
            if target >= i[0] and target <= i[len(i)-1]:
                element_row = i
                break
            
        if element_row == []:
            return False

        l, r = 0, len(element_row) - 1

        while (l<=r):
            mid = (l+r)//2
            if element_row[mid] == target:
                return True
            elif element_row[mid] < target:
                l = mid + 1
            elif element_row[mid] > target:
                r = mid - 1
        return False
        