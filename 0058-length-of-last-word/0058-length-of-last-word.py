class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        start = 0
        end = 0
        for i in range(n - 1, -1, -1):
            if s[i] != " ":
                end = i
                break
        
        for j in range(end, -1, -1):
            if s[j] == " ":
                start = j
                break
            if j == 0:
                start = -1
        
        return end - start


