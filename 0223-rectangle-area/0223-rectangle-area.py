class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        a_area = abs(ax2 - ax1) * abs(ay2 - ay1)
        b_area = abs(bx2 - bx1) * abs(by2 - by1)
        
        x_overlap = min(ax2, bx2) - max(ax1, bx1)
        y_overlap = min(ay2, by2) - max(ay1, by1)
        
        overlap_area = 0
        
        if x_overlap > 0 and y_overlap > 0:
            overlap_area = x_overlap * y_overlap
        
        return a_area + b_area - overlap_area
        
        