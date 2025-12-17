class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set() #  cols occupied
        diag1 = set() # r - c
        diag2 = set() # r + c
        ans = 0

        def backtrack(row):
            nonlocal ans
            if row == n:
                ans += 1
                return
            
            for col in range(n):
                if col in cols: continue
                d1 = row - col
                if d1 in diag1: continue
                d2 = row + col
                if d2 in diag2: continue

                # thoes who not "continue" can add to the set
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)
        
        backtrack(0)
        return ans
            

                    

