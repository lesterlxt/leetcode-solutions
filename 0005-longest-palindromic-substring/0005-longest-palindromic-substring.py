class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = 1
        start = 0

        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] == 1:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        
        return s[start : start + max_len]




