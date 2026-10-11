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
                elif (j-i) == 1 or (j-i) == 2 :
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
    """
            memo = {}
        maxi = 0
        couple = (0,0)
        n = len(s)
        for i in range(n):
            memo[(i,i)] = True
            if i+1 < n:
                memo[(i, i+1)] = (s[i] == s[i+1])
            if i+2 < n:
                memo[(i, i+2)] = (s[i] == s[i+2])
        
        def dp(i,j):
            nonlocal maxi, couple
            if (i,j) in memo:
                if memo[(i,j)] and (j-i)>maxi:
                    maxi  = j-i
                    couple = (i,j)
                return memo[(i,j)]

            memo[(i,j)] = (s[i] == s[j] and dp(i+1, j-1))
            if memo[(i,j)] and (j-i)>maxi:
                maxi  = j-i
                couple = (i,j)
            return memo[(i,j)]

        for i in range(n):
            for j in range(i, n):
                dp(i, j)
        return s[couple[0]: couple[1]+1]
        



        """
        