class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX = max(x1, min(x2, xCenter))
        closestY = max(y1, min(y2, yCenter))

        xDiff = abs(xCenter - closestX)
        yDiff = abs(yCenter - closestY)

        return xDiff**2 + yDiff**2 <= radius**2