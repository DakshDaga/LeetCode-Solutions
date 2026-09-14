class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, x2, y1, y2 = rec1[0], rec1[2], rec1[1], rec1[3]
        x3, x4, y3, y4 = rec2[0], rec2[2], rec2[1], rec2[3]

        if x1>=x4 or x2<=x3 or y1>=y4 or y2<=y3:
            return False
        return True