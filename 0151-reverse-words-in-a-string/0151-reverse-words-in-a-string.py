class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        l, r = 0, len(s) - 1

        while r >= 0:
            if s[r] != " ":
                l = r
                while l >= 0 and s[l] != " ":
                    l -= 1
                words.append(s[l + 1: r + 1])
                r = l
            else:
                r -= 1
        
        return " ".join(words)
        