class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        max_size = float("-inf")
        couple = (0,0)
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if (j-i) == 0:
                    dp[i][j] = True
                elif (j-i) == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                elif j-i == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                elif (j-i) > 2:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = 0
                if dp[i][j] and (j-i) > max_size:
                    max_size = j - i
                    couple = (i,j)
        return s[couple[0]: couple[1]+1]
        