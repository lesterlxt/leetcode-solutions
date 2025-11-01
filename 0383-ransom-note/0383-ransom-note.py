class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        cnt = [0] * 26
        for ch in magazine:
            cnt[ord(ch) - 97] += 1
        
        for ch in ransomNote:
            i = ord(ch) - 97
            cnt[i] -= 1
            if cnt[i] < 0:
                return False
        
        return True