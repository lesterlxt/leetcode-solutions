class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            s = 0
            while x > 0:
                d = x % 10
                s += d * d
                x = x // 10
            return s
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_num(n)
        
        return n == 1
        

