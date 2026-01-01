class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 0
        for i in range(n):
            slopes = defaultdict(int)
            same = 0
            cur_max = 0

            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dy = y2 - y1
                dx = x2 - x1
                
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                
                if dx == 0:
                    slope = (1, 0)    
                
                elif dy == 0:
                    slope = (0, 1)
                
                else:
                    g = math.gcd(dx, dy)
                    dx = dx // g
                    dy = dy // g
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slope = (dy, dx)

                slopes[slope] += 1
                cur_max = max(cur_max, slopes[slope])
            
            ans = max(ans, cur_max + same + 1)
        
        return ans
            






