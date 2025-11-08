class Solution:
    def isHappy(self, n: int) -> bool:
        def sqsum(x: int) -> int:
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s
    
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sqsum(n)
        return n == 1
