class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen  = set()

        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l += 1
            seen.add(ch)
            res = max(res, r - l + 1)
        
        return res