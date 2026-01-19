class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        for i in range(n):
            ch = strs[0][i]
            for s in strs:
                if i > len(s) - 1 or ch != s[i]:
                    return s[:i]
    
        return strs[0]