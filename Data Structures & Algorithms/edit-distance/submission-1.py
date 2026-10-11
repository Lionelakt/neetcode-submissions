class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        if n1 < n2:
            return self.minDistance(word2, word1)
            
        dp = list(range(n2 + 1))
        
        for i in range(1, n1 + 1):
            diag = dp[0]  # Sauvegarde dp[i-1][0]
            dp[0] = i     # Devient dp[i][0]
            
            for j in range(1, n2 + 1):
                temp = dp[j]  # C'est l'ancien dp[i-1][j], qui sera le diag de la prochaine colonne
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = diag
                else:
                    dp[j] = 1 + min(
                        diag,      # dp[i-1][j-1]
                        dp[j],     # dp[i-1][j]
                        dp[j - 1]  # dp[i][j-1]
                    )
                diag = temp
                
        return dp[n2]