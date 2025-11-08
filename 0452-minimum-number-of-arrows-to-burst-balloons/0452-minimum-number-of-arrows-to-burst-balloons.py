class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return []
        
        points.sort(key=lambda p: p[1])
        arrows = 1
        shoot_x = points[0][1]

        for start, end in points[1:]:
            if start <= shoot_x:
                continue
            arrows += 1
            shoot_x = end
        
        return arrows
            