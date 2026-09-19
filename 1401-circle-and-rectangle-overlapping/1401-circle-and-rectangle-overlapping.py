class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        # Closest point on the rectangle to the circle's center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Distance squared between circle center and closest point
        dx = xCenter - closestX
        dy = yCenter - closestY

        distanceSquared = dx * dx + dy * dy

        # If distance <= radius, they overlap
        return distanceSquared <= radius * radius
        