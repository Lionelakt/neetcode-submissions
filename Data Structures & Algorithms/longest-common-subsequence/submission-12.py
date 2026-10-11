class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2) 
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        if n1==0 or n2==0:
            return 0
        dp[0][0] = 0
        for i in range(1,n1+1):
            dp[i][0] = 0
        for j in range(1,n2+1):
            dp[0][j] = 0

        for i in range(1, n1+1):
            for j in range(1,n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
