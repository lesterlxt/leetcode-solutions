class Solution:
    def mySqrt(self, x: int) -> int:
        num = 1
        res = 0
        while x >= num * num:
            res = num
            num += 1
        return res

