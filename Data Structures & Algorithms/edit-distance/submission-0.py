class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[None]*(1+n2) for _ in range(1+n1)]

        #Base case
        dp[0][0] = 0
        for j in range(1, n2+1):
            dp[0][j] = j
        for i in range(1, n1+1):
            dp[i][0] = i

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min((dp[i-1][j-1], 
                    dp[i-1][j],dp[i][j-1])) 
        return dp[n1][n2]