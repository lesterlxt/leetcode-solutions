class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        
        direction = 1
        row = 0
        res = [""] * numRows

        for i in range(len(s)):
            res[row] += s[i]
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
        
        return "".join(res)
