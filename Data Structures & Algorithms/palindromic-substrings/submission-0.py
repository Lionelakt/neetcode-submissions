
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        number = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if (j-i) == 0:
                    dp[i][j] = True
                elif (j-i) == 1:
                    dp[i][j] = s[i] == s[j]
                elif (j-i) == 2:
                    dp[i][j] = (s[i]==s[j])
                else:
                    dp[i][j] = dp[i+1][j-1]\
                    if s[i] == s[j] else False  

                number += dp[i][j]
        return number