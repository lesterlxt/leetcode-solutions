class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            if height[l] < height[r]:
                water = height[l] * (r - l)
                res = max(res, water)
                l += 1
            else:
                water = height[r] * (r - l)
                res = max(res, water)
                r -= 1

        return res

        