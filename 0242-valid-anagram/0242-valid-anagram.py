class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt = [0] * 26
        base = ord('a')
        for ch in s:
            cnt[ord(ch) - base] += 1
        for ch in t:
            cnt[ord(ch) - base] -= 1
            if cnt[ord(ch) - base] < 0:
                return False
        
        return True